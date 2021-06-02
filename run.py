"""
    Файл запуска приложения
"""

if __name__ == '__main__':
    import os, sys
    from src import Application
    
    app = Application(os.path.dirname(__file__), sys.argv)
    sys.exit(app.exec_())