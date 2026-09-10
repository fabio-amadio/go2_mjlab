# go2-mjlab

<table>
  <tr>
    <td width="50%">
      <video src="https://github.com/user-attachments/assets/fcb17cde-62ed-4dce-ae00-c3adbb6593e2" controls muted playsinline style="width:100%; height:auto;"></video>
    </td>
    <td width="50%">
      <video src="https://github.com/user-attachments/assets/9035d76c-5730-4ebe-a8c3-199806980bcf" controls muted playsinline style="width:100%; height:auto;"></video>
    </td>
  </tr>
</table>


Standalone Unitree Go2 velocity environments for
[mjlab](https://pypi.org/project/mjlab/).

This package depends on the published `mjlab` package and registers two task IDs:

- `Mjlab-Velocity-Flat-Unitree-Go2`
- `Mjlab-Velocity-Rough-Unitree-Go2`

## Setup

```sh
uv sync
```

## Commands

List environments:

```sh
uv run list-envs --keyword Go2
```

Play with a random agent:

```sh
uv run play Mjlab-Velocity-Flat-Unitree-Go2 --agent random
```

Train:

```sh
uv run train Mjlab-Velocity-Rough-Unitree-Go2 --env.scene.num-envs 4096 --agent.logger tensorboard
```

Play a trained checkpoint:

```sh
uv run play Mjlab-Velocity-Rough-Unitree-Go2 --checkpoint-file logs/rsl_rl/go2_velocity/<run>/model_<step>.pt
```

Raw env rollout:

```sh
uv run rollout
```
