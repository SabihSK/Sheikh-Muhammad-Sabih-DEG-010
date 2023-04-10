import typer


def main(name: str = typer.Option('...'), name1: str = typer.Option(...)):
    print(f"Hello {name} and {name1}")


if __name__ == "__main__":
    typer.run(main)
