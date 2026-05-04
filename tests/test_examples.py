import json
from pathlib import Path

BASE_DIR = Path('examples/deep_slot_button')
EXAMPLES = [
    'deep_slot_button_success',
    'deep_slot_button_short_tool_fail',
    'deep_slot_button_tweezer_fail',
]
JSON_FILES = [
    'scene_info.json',
    'toig.json',
    'decision_oracle.json',
    'grounded_contract.json',
    'tool_memory_episode.json',
]


def _load_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def test_all_json_files_load_and_have_required_top_level_fields():
    required_fields = {
        'scene_info.json': ['example_id', 'task', 'robot', 'object', 'placeholders'],
        'toig.json': ['task', 'instance_id', 'goal', 'tool_candidates', 'environment_constraints'],
        'decision_oracle.json': ['example_id', 'selected_tool', 'success', 'reasoning'],
        'grounded_contract.json': ['example_id', 'selected_tool', 'execution_constraints', 'expected_outcome'],
        'tool_memory_episode.json': ['episode_id', 'task', 'selected_tool', 'result', 'observation_summary'],
    }

    for example in EXAMPLES:
        for filename in JSON_FILES:
            path = BASE_DIR / example / filename
            assert path.exists(), f'Missing file: {path}'
            data = _load_json(path)
            for field in required_fields[filename]:
                assert field in data, f'Missing field {field} in {path}'


def test_selected_tool_consistency_between_oracle_and_contract():
    for example in EXAMPLES:
        oracle = _load_json(BASE_DIR / example / 'decision_oracle.json')
        contract = _load_json(BASE_DIR / example / 'grounded_contract.json')
        assert oracle['selected_tool'] == contract['selected_tool']


def test_success_and_failure_examples_are_labeled_correctly():
    success_oracle = _load_json(BASE_DIR / 'deep_slot_button_success' / 'decision_oracle.json')
    assert success_oracle['success'] is True

    for example in ['deep_slot_button_short_tool_fail', 'deep_slot_button_tweezer_fail']:
        oracle = _load_json(BASE_DIR / example / 'decision_oracle.json')
        assert oracle['success'] is False
        assert oracle.get('failure_type'), f'failure_type required for {example}'
        assert oracle.get('correction'), f'correction required for {example}'
