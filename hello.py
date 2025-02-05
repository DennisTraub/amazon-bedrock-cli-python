from amazon_bedrock import Bedrock


def main():
    client = Bedrock()
    models = client.models.list()
    print(models)


if __name__ == "__main__":
    main()
