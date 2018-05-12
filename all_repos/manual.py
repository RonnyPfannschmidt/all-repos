import argparse

from all_repos import autofix_lib


def find_repos(_):
    raise AssertionError('--repos is required')


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Interactively apply a manual change across repos.',
        usage='%(prog)s [options]',
    )
    autofix_lib.add_fixer_args(parser)
    parser.add_argument(
        '--branch-name', default='all-repos-manual',
        help='override the autofixer branch name (default `%(default)s`).',
    )
    parser.add_argument(
        '--commit-msg', required=True,
        help='set the autofixer commit message.',
    )
    args = parser.parse_args(argv)

    # force interactive
    args.interactive = True

    repos, config, commit, autofix_settings = autofix_lib.from_cli(
        args,
        find_repos=find_repos,
        msg=args.commit_msg,
        branch_name=args.branch_name,
    )

    autofix_lib.fix(
        repos,
        apply_fix=autofix_lib.shell,
        config=config,
        commit=commit,
        autofix_settings=autofix_settings,
    )


if __name__ == '__main__':
    exit(main())
