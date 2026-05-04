# Deep Slot Button Example Dataset

This directory contains three Tool Cognition VLA pipeline examples for a deep slot button task.

## Examples

- `deep_slot_button_success`: `long_screwdriver` succeeds.
- `deep_slot_button_short_tool_fail`: `short_screwdriver` fails with `insufficient_length`.
- `deep_slot_button_tweezer_fail`: `tweezer` fails with `unstable_press` when using a parallel gripper.

Each example includes:

- `scene_info.json`
- `toig.json`
- `decision_oracle.json`
- `grounded_contract.json`
- `tool_memory_episode.json`

And placeholder data directories:

- `images/`
- `masks/`
- `poses/`
- `frames/`
- `trajectories/`
- `force_traces/`

All paths are placeholders and intentionally do not reference real binary data.
