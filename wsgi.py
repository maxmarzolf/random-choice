from app import create_app

import config

app = create_app(config.Test(no_db=False))

if __name__ == "__main__":
    app.run()
