from views.main_view import MainView
from dao.database import init_db

# Inicializa o banco ao iniciar o programa
init_db()


if __name__ == "__main__":
    app = MainView()
    app.mainloop()