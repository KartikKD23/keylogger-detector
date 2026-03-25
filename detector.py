import psutil

suspicious_keywords = ["keylog", "hook", "capture", "spy"]

def get_processes():
    results = []

    for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            name = process.info['name'].lower()
            pid = process.info['pid']
            cpu = process.info['cpu_percent']

            keyword_flag = 0
            for keyword in suspicious_keywords:
                if keyword in name:
                    keyword_flag = 1

            results.append((name, pid, cpu, keyword_flag))

        except:
            continue

    return results