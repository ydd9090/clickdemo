import click


@click.command()
@click.option("--string",default="click",help="console will print this string.")
@click.option("--repeat",default=1,help="")
def cli(string,repeat):
    for i in range(repeat):
        print("Hello {}".format(string))