project('bureau',
          version: '0.1.0',
    meson_version: '>= 0.62.0',
  default_options: [ 'warning_level=2', 'werror=false', ],
)

author = 'tenderowl'
domain = 'com.'
# app_id built as: domain.author.project_name
gitrepo = 'https://github.com/'+author+'/'+meson.project_name()
website = 'https://tenderowl.com'


i18n = import('i18n')
pymod = import('python')
gnome = import('gnome')

python = pymod.find_installation()
prefix = get_option('prefix') # should be /usr
bindir = get_option('bindir') # should be bin
datadir = get_option('datadir') # should be /usr/share
pkgdatadir = prefix / datadir / meson.project_name()
pythondir = python.get_install_dir()
localedir = prefix / get_option('localedir')


install_subdir(meson.project_name(), install_dir: pythondir)
subdir('data')
subdir('bin')
subdir('po')

gnome.post_install(
     glib_compile_schemas: true,
    gtk_update_icon_cache: true,
  update_desktop_database: true,
)
