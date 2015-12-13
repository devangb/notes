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
		current_branch = master
	else:
		click.echo("Notes already initiated.")



@cli.command()
@click.option('-b', is_flag=True)
@click.argument('branch',required=True)
def checkout(branch,b):
	branch_dir = './.notes/'+branch
	if b:
		if not os.path.exists(branch_dir):
			os.makedirs(branch_dir)
			click.echo("Created and switched to branch - "+ branch)
		else:
			click.echo("Branch already exists")
			click.echo("Switched to branch - "+ branch)
		current_dir = branch_dir
		current_branch = branch
	else:
		if not os.path.exists(branch_dir):
			click.echo("Branch does not exist. Use \"notes checkout -b branch\" to create the branch first")
		else:
			current_dir = branch_dir
			current_branch = branch



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
