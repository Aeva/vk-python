
import subprocess
import glob


def build(src, stage):
    args = ["glslc", "-c", "-std=420", f"-fshader-stage={stage}", src]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError:
        print(" ".join(args))


if __name__ == "__main__":
    build("test.vs.glsl", "vertex")
    build("test.fs.glsl", "fragment")
