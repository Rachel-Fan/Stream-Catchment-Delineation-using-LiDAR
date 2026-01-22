from workflow.prep.step01_prepare_urls import run_step01
from workflow.prep.step03_unzip_tiles import run_step03
from workflow.prep.step04_mosaic_tiles import run_step04

STEP_REGISTRY = {
    1: run_step01,
    3: run_step03,
    4: run_step04,
}

def run_steps(step_numbers, config):
    for step in step_numbers:
        print(f"\n=== Running Step {step:02d} ===")
        STEP_REGISTRY[step](config)


if __name__ == "__main__":
    config = load_config_somehow()

    # examples:
    run_steps([3], config)           # only unzip
    run_steps([3, 4], config)        # unzip + mosaic
    run_steps([1, 3, 4], config)     # skip UGET (step 2)
