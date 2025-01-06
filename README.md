# Big Pal Project
The `Big Pal Project` is a mod for Pal World that adds in a simple weight gain system so pals can gain and lose weight.

This project contains two sub projects, [big-pal-models] which holds the models and [big-pal-system] which holds the game logic.

https://forum.weightgaming.com/t/big-pal-project-0-5-a-weight-gain-mod-for-palworld-5-8-update/40309

## Install Instructions
### Mod Install
1. Download and install [UE4SS](https://github.com/UE4SS-RE/RE-UE4SS/releases/) into Palworld (this is needed for the WG System mod)
2. Once [UE4SS](https://github.com/UE4SS-RE/RE-UE4SS/releases/) is installed run the game and load a world once. Your game may crash on the first load, but this is normal. Just try to restart the game and reload the world.
3. Go to your Palworld install directory and navigate to `Pal\Content\Paks`. If [UE4SS](https://github.com/UE4SS-RE/RE-UE4SS/releases/) installed correctly you should see a `LogicMods` folder in there along with a `Pal-Windows.pak` file which is for the base game.
4. Download the latest big pal project zip from the [releases section](#releases-1) and copy its contents to the `Pal\Content\Paks`
5. Start your game and you should be done!

### Dev Setup
1. Install Unreal Engine 5.1 if not already installed
2. Clone or download this repo
  - **NOTE:** If you choose to use git to clone the repo, you need git LFS enabled to pull down the `fbx` files.
3. Install the Wwise plugin into [big-pal-system]. Instructions can be found [here](https://pwmodding.wiki/docs/palworld-modding-kit/install-part-1#wwise).
4. You should be able to now open the unreal project for either [big-pal-models] or [big-pal-system].
5. Enable python tools in UE to make use of the custom tools and build scripts if not already enabled.

See the projects respective READMEs for more information.

### Known Issues
- When opening [big-pal-system] for the first time it will prompt to you recompile. Sometimes this fails and requires to be opened and recompiled again.
- Sometimes [big-pal-system] fails to rebuild due to failing to build the `CapsuleTraceRotation` plugin under the `EnginePlugins` directory. I do not know what causes this but may be a BOM or formatting issue with the source code. Copying the files to another directory and then back seems to fix it.

## [big-pal-models]
This project is for the model replacement pak for the modified models. The `models` folder contains the raw modified models in either a `.fbx` format or as a `.blend`. The `Pal` folder contains the unreal project that creates the pak file. See the [README](https://github.com/grotlover2/Big-Pal-Project/blob/main/big-pal-models/README.md) for more information.

## [big-pal-system]
This project holds the game logic portion of the mod that modifies the shape keys on the pal models. The game logic makes use of [UE4SS](https://github.com/UE4SS-RE/RE-UE4SS) and the [PalworldModdingKit](https://github.com/localcc/PalworldModdingKit) to create a `blue print` mod to be injected into the game at runtime. See the [README](https://github.com/grotlover2/Big-Pal-Project/blob/main/big-pal-system/README.md) for more information.

## Contributions
All current and future contributions are under the MIT or CC0 licenses, whichever is most appropriate for that contribution.

## Useful Modding Resources
https://pwmodding.wiki/docs/intro

https://youtu.be/NESKhITrbgI

https://docs.ue4ss.com/dev/guides/creating-a-c++-mod.html

https://docs.ue4ss.com/index.html

https://github.com/KURAMAAA0/PalModding/blob/main/PalNamesCodeNames.txt

https://pwmodding.wiki/docs/game-data/monster-table

## Original Team Credits
### 3D Modeling
- ExtrudedSquared
- vzojin
- LordOfDeez
- Thickglacier
- KeaBuns

### Programing
- grotlover2
- Niwatori401

## FAQ
- Can I use this in multiplayer?
  - Yes, the mod is currently client side only so should be able to be used in multiplayer games without much issue

- My game crashed, should I be concerned?
  - No, this sometimes happens epsically after updating the _P .pak files. Just restart and should be fairly stable. That being said we have had some reports of some saves just refusing to work with the mod. We dont know what causes it but if it gives you a ton of issues you may need to just create a new world as that usually fixes it.

- Are you all going to add more pals?/Are these models final?
  - Unfortunately, there are no plans to add any more pals or clean up any of the current models.

- Are you planing on expanding the system?
  - No. We wanted to implement a more in depth weight gain system but after looking into it we found that it would be to difficult to do what we wanted to do with the current setup of PalWorld and we could not figure out how to make it MP compatible without doing some weird hacks. Maybe if an official modding API is released or there are further developments to the PMK that could support the features we wanted I may reevaluate it.

- Are there plans for the players to also gain weight?
  - No, not at the moment at least. We did evaluate it and think it is possible to do that, but we never got anyone to modify the models for it. If some one provides modified player models with the expected shape keys I could look back into it.

- Why was the project moved to open source?
  - The main reason is development stalled out, mainly with creating new models. By open sourcing the project we hope that some development can continue by allowing community members to contribute to the project if they wish.

- Will the project continue to be maintained?
  - Yes, or at least best I can. I plan on trying to keep the mod up to date with PalWorld's updates as I can.

- Pal X looks to be broken/their textures are broken. Will they be fixed?
  - Unfortunately, fixing the models is a bit out of my wheelhouse. But I will happily accept any PRs that do fix them.

- Can I contribute new models or content to the mod?
   - Yes! If you want to clean up a model, add a new pal, or anything else feel free to do so and make a PR for it! If you have any questions or need any help feel free reach out to me on here, [twitter](https://twitter.com/grotlover2), or discord and I will be happy to help however I can.

- What if I want to do only my own models/do my own thing?
  - Yes, you can do that! You can either fork this project if you want full control or you can create a new model replacement pak with your own models and use our [big-pal-system]. See [big-pal-models] for more information on replacing models and setting them up to work with the [big-pal-system].

- Can I do inflation/muscle expansion/some other growth or expansion with this system?
  - I would need to consider if we would want to include multiple expansion options in the mod proper, but for personal use yes, you just need to modify the models to look the way you want. As long as they have the required shape keys on them the system will adjust what ever expansion you decided to do with the pals hunger. See the [big-pal-models] project for more details.

- I dont see a pal on the issue board. Should it be on there?
  - The issue board is not an exhaustive list of all the pals and is really only up to date for when the project was started. If you see a pal missing feel free to add it to the board.

- I found a bug, what should I do?
  - Open an issue for it and label it as a bug. If its anything code or configuration related I will try to fix it but no promises for anything model related.

[big-pal-models]: https://github.com/grotlover2/Big-Pal-Project/tree/main/big-pal-models
[big-pal-system]: https://github.com/grotlover2/Big-Pal-Project/tree/main/big-pal-system