import psutil


class OSController:
    @staticmethod
    def get_all_processes() -> dict[int, str]:
        return {pid: psutil.Process(pid).name() for pid in psutil.pids()}

    @staticmethod
    def kill_process(pid: int) -> None:
        p = psutil.Process(pid)
        p.terminate()
        p.wait()

