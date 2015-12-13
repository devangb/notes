import click

@click.group()
def cli():
	pass


@cli.command()
def init():
	pass



@cli.command()
@click.argument('branch',required=True)
def checkout(branch):
	pass


@cli.command()
@click.argument('title',required=True)
@click.argument('content',required=True)
def new(title, content):
	click.echo(title + ' ' + content)


@cli.command()
def merge():
	pass

@cli.command()
def show():
	pass

@cli.command()
def edit():
	pass

@cli.command()
def archive():
	pass

@cli.command()
def delete():
	pass
