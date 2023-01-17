import click



@click.group()
@click.option("--verbose",is_flag=True,)
def cli(verbose):
    if verbose:
        click.echo("We are in verbose mode.")

@cli.command()
@click.option("--string",default="click",help="打印该字符串")
@click.option("--repeat",default=1,help="重复打印次数")
@click.argument("out",type = click.File("w"),required=False)
def say(string,repeat,out):
    for i in range(repeat):
        click.echo("Hello {}".format(string))
        if out:
            click.echo("Hello {}".format(string),file=out)