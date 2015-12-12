import click

@click.group()
def cli():
	pass

@cli.command()
@click.argument('title',required=True)
@click.argument('content',required=True)
def new(title, content):
	click.echo(title + ' ' + content)
