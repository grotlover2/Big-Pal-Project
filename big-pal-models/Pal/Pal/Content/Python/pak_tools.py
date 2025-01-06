import glob
import os
import pathlib
import shutil

import unreal
import pak_config

eal = unreal.EditorAssetLibrary()

PROJECT_DIR = pathlib.Path(unreal.Paths.get_project_file_path()).parent.absolute().resolve()
COOKED_CONTENT_DIR = f'{PROJECT_DIR}/Saved/Cooked/Windows'
MOD_DIR = f'{PROJECT_DIR}/Mod'
DBG_PAK_DIR = f'{PROJECT_DIR}/Mod/dbg'


def process_models():
    build_skeleton_dir()
    # rename_assets()
    move_skeletons()


def build_pak():
    unreal.log('Building Paks...')
    clean_mod_dir()
    copy_cooked_files_to_mod_dir()
    package_files()


def build_skeleton_dir():
    for folder in _get_monster_dirs():
        folder_path = pathlib.Path(folder)
        skeleton_dir = f'/Game/Pal/Model/Character/Skeleton/{folder_path.name}'
        if not eal.does_directory_exist(skeleton_dir):
            unreal.log(f'Creating {skeleton_dir}')
            eal.make_directory(skeleton_dir)
        else:
            unreal.log(f'{skeleton_dir} exists, skipping...')


def rename_assets():
    eul = unreal.EditorUtilityLibrary
    for folder in _get_monster_dirs():
        folder_path = pathlib.Path(folder)
        asset_name = folder_path.name
        for asset in eal.list_assets(folder):
            asset_path = pathlib.Path(asset)
            data = eal.find_asset_data(str(asset_path))
            asset_class = data.asset_class_path.asset_name

            if asset_class == 'SkeletalMesh':
                new_name = f'SK_{asset_name}'
                unreal.log(f'Renaming {asset_path.name} to {new_name}')
                eul.rename_asset(eal.load_asset(asset), new_name)
            elif asset_class == 'Skeleton':
                new_name = f'SK_{asset_name}_Skeleton'
                unreal.log(f'Renaming {asset_path.name} to {new_name}')
                eul.rename_asset(eal.load_asset(asset), new_name)
            elif asset_class == 'PhysicsAsset':
                new_name = f'PA_{asset_name}_PhysicsAsset'
                unreal.log(f'Renaming {asset_path.name} to {new_name}')
                eul.rename_asset(eal.load_asset(asset), new_name)


def move_skeletons():
    for folder in _get_monster_dirs():
        folder_path = pathlib.Path(folder)
        asset_name = folder_path.name
        for asset in eal.list_assets(folder):
            asset_path = pathlib.Path(asset)
            data = eal.find_asset_data(str(asset_path))
            asset_class = data.asset_class_path.asset_name
            if asset_class == 'Skeleton':
                skeleton_dir = f'/Game/Pal/Model/Character/Skeleton/{asset_name}/{asset_path.name}'
                unreal.log(f'Moving {asset_path.name} to {skeleton_dir}...')
                eal.rename_asset(str(asset_path), skeleton_dir)


def clean_mod_dir():
    unreal.log(f'Cleaning {MOD_DIR}...')
    shutil.rmtree(f'{MOD_DIR}/FatPals_P/Pal', ignore_errors=True)
    shutil.rmtree(f'{MOD_DIR}/dbg', ignore_errors=True)
    os.makedirs(f'{MOD_DIR}/dbg', exist_ok=True)


def copy_cooked_files_to_mod_dir():
    files = []
    for skeletal_mesh_uasset in glob.glob(f'{COOKED_CONTENT_DIR}/**/*.uasset', recursive=True):
        files.append(skeletal_mesh_uasset)
    for skeletal_mesh_uexp in glob.glob(f'{COOKED_CONTENT_DIR}/**/*.uexp', recursive=True):
        files.append(skeletal_mesh_uexp)

    for file in files:
        f = pathlib.Path(file)
        if f.name.startswith('SK_') and ('\\Monster\\' in file or '/Monster/' in file):
            pak_name = f.parts[-2]
            base_dir = file.replace(f'{COOKED_CONTENT_DIR}\\Pal\\', '')
            _copy_to(file, f'{MOD_DIR}/dbg/{pak_name}_P/Pal/{base_dir}')
            if pak_config.config[pak_name]['release']:
                _copy_to(file, f'{MOD_DIR}/FatPals_P/Pal/{base_dir}')


def package_files():
    pack_bat = f'{MOD_DIR}/UnrealPak/UnrealPak-With-Compression.bat'
    unreal.log('Creating the mod pak...')
    os.system(f'{pack_bat} {MOD_DIR}/FatPals_P')
    unreal.log('Creating debug paks...')
    for dbg_path in glob.glob(f'{MOD_DIR}/dbg/*'):
        unreal.log(f'Packaging {dbg_path}...')
        os.system(f'{pack_bat} {dbg_path}')
    unreal.log('Done')


def _get_monster_dirs():
    for path in eal.list_assets('/Game/Pal/Model/Character/Monster', include_folder=True):
        if path.endswith('/'):
            yield path


def _copy_to(src, dst):
    unreal.log(f'Copying {src} to {dst}...')
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy(src, dst)
