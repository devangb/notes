import click
import os

@click.group()
def cli():
	pass


@cli.command()
def init():
	directory = './.notes/master'
	if not os.path.exists(directory):
		os.makedirs(directory)
	else:
		click.echo("Notes already initiated.")



@cli.command()
@click.option('-b', is_flag=True)
@click.argument('branch',required=True)
def checkout(branch,b):
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
