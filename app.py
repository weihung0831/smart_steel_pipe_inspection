import eel

@eel.expose  # 用decorator的方式，將JS要呼叫的PY function暴露給eel, 讓eel當作一個library  去給JS使用
def say_something(word):
    # 返回 字串加上被呼叫的次數
    return (
        f"{word}"
    )


eel.init("web")  # 設定web的資料夾路徑
eel.start("main.html")  # 設定要開啟的html檔案路徑
