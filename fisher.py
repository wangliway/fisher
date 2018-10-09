from app import create_app

app = create_app()


if __name__ == '__main__':
    # host 接收外网的访问
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])
