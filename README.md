# Unreal TD Test Submission

---

## 1️⃣ Workflow - Pipeline Visualization

I have committed here. In the first folder in the github there is a pdf that can be downloaded "01_Workflow": https://github.com/adamvirtualspace-lab/adamunrealpipelinetdtest/tree/main/01_Workflow

There's also an online version available on Milanote: https://app.milanote.com/1W0YJG1oCvCK6V?p=hLiaRMOpPQY

![Pipeline Workflow Preview](https://raw.githubusercontent.com/adamvirtualspace-lab/adamunrealpipelinetdtest/refs/heads/main/01_Workflow/IdealPipelineImageOnlyPreview/IdealPipelineImageOnlyPreview.PNG)

The flowchart covers each stage from concept design and character drawing through rigging, animation approval, and final scene integration. It includes decision points for approval and revision cycles that occur in production workflows.

---

## 2️⃣ Assets - Character Rigging

In the second folder of the github (02_Assets): https://github.com/adamvirtualspace-lab/adamunrealpipelinetdtest/tree/main/02_Assets I have uploaded both the blender rig and the exported skeletal mesh. For the imported version of the skeletal mesh, it's in the third folder where I uploaded the whole unreal project along with the playblast tools & effects.

![Skeletal Mesh Preview](https://raw.githubusercontent.com/adamvirtualspace-lab/adamunrealpipelinetdtest/refs/heads/main/02_Assets/BlenderUnrealSkeletalAssetPreview.png)

The skeletal structure supports animation with proper bone chains for spine, arms, and legs. Weight painting has been applied for natural deformation during animation.

---

## 3️⃣ Animation - Playblast Tool

I have built a scriptable tool where we can mass select level sequences, right click and hit "Do Playblast for Selected Level Sequence". It's in the third github folder (03_AnimationPlayblastUEProjects): https://github.com/adamvirtualspace-lab/adamunrealpipelinetdtest/tree/main/03_AnimationPlayblastUEProjects

![Playblast Right-Click Menu](https://raw.githubusercontent.com/adamvirtualspace-lab/adamunrealpipelinetdtest/refs/heads/main/03_AnimationPlayblastUEProjects/RightClickPlayblastForAllSelectedLS.png)

**How it works:**

Simply multiple select level sequences, right click and hit the scripted asset action "Do Playblast for Selected Level Sequence". The tool automatically:
- Creates necessary job entries
- Generates output asset directories for the movie render queue
- Detects and sets the asset directory path
- Allows customization through the default playback tools settings

**Burn-in information:**

The tool can be configured to display burn-in metadata on the rendered preview, including:
- Frame number
- Shot name
- Focal length
- Date and job name
- User and computer information
- All other level sequence metadata

The tool uses optimized render settings for fast preview generation while maintaining clarity for review purposes.

---

## 4️⃣ Visual Effects - Dust Particles

I have rendered the FX preview mov, where dust is emitted when character hits the dust area and the dust emitter attached to the character's feet. It's in the fourth github folder (04_FX): https://github.com/adamvirtualspace-lab/adamunrealpipelinetdtest/tree/main/04_FX

**Setup:**
- Niagara module stack configured with spawn rate, position, velocity, lifetime, and color
- Emitter attached to foot bone socket for character-relative movement
- Particles spawn with downward velocity for ground-kicking effect
- Physics interaction included

The effect provides visual feedback for character locomotion and ground contact.

---

## 5️⃣ Programming - Python Scripts

For A & B I have committed in the 5th folder (05_PyScripts): https://github.com/adamvirtualspace-lab/adamunrealpipelinetdtest/tree/main/05_PyScripts

Inside there's "05A_PatternB.py" where the script generate star pattern and the "05B_CharNamesCorrecter.py" where I corrected the name corrector.

### 5A - Pattern Generation (`05A_PatternB.py`)

This script generates ASCII art using nested loops to create a symmetric diamond pattern. The outer edge uses "x" characters while inner layers use "—" characters to form geometric shapes.

**Output preview:**
```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxx----xxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxx--xxxx--xxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxx------------xxxxxxxxxxxxxxxx------------xxxxxxxxxx
xxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxx
xxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxx
xxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxx
xxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxx
xxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxx
xxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxx
xxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxx
xxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxx
xx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xx
--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--
xx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xx
xxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxx
xxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxx
xxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxx
xxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxx
xxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxx
xxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxx
xxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxx
xxxxxxxxxx------------xxxxxxxxxxxxxxxx------------xxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxx--xxxxxxxxxxxx--xxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx--xxxxxxxx--xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxx--xxxx--xxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxx----xxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5B - Character Names Corrector (`05B_CharNamesCorrecter.py`)

The original code demonstrated a late binding closure issue in Python. All lambda functions were referencing the same variable `n`, which pointed to the last list item after loop completion.

**Original Problem:**
```python
funcs.append(lambda: string_appender(n, "char"))
# All lambdas reference final value of n: "bob"
```

**Solution:**
```python
funcs.append(lambda n=n: string_appender(n, "char"))
# Default argument captures value at function definition time
```

Using a default argument forces Python to capture the current value of `n` at lambda creation, rather than at execution. Each lambda now retains its own reference to the correct name.

---

## Overview

This submission demonstrates the interconnected aspects of a production pipeline. Each component—workflow documentation, asset preparation, animation tools, visual effects, and programming—supports the larger system. The tool development shows understanding of production efficiency, while the technical implementations showcase both artistic and technical capability.

---

## Resources

- **Main Repository:** https://github.com/adamvirtualspace-lab/adamunrealpipelinetdtest
- **Workflow Visualization:** https://app.milanote.com/1W0YJG1oCvCK6V?p=hLiaRMOpPQY