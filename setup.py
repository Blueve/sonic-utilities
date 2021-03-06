# https://github.com/ninjaaron/fast-entry_points
# workaround for slow 'pkg_resources' import
#
# NOTE: this only has effect on console_scripts and no speed-up for commands
# under scripts/. Consider stop using scripts and use console_scripts instead
#
# https://stackoverflow.com/questions/18787036/difference-between-entry-points-console-scripts-and-scripts-in-setup-py
try:
    import fastentrypoints
except ImportError:
    from setuptools.command import easy_install
    import pkg_resources
    easy_install.main(['fastentrypoints'])
    pkg_resources.require('fastentrypoints')
    import fastentrypoints

from setuptools import setup

setup(
    name='sonic-utilities',
    version='1.2',
    description='Command-line utilities for SONiC',
    license='Apache 2.0',
    author='SONiC Team',
    author_email='linuxnetdev@microsoft.com',
    url='https://github.com/Azure/sonic-utilities',
    maintainer='Joe LeVeque',
    maintainer_email='jolevequ@microsoft.com',
    packages=[
        'acl_loader',
        'clear',
        'config',
        'connect',
        'consutil',
        'counterpoll',
        'crm',
        'debug',
        'pfcwd',
        'sfputil',
        'ssdutil',
        'pfc',
        'psuutil',
        'fdbutil',
        'fwutil',
        'pcieutil',
        'pddf_fanutil',
        'pddf_psuutil',
        'pddf_thermalutil',
        'pddf_ledutil',
        'show',
        'show.interfaces',
        'sonic_installer',
        'sonic_installer.bootloader',
        'tests',
        'undebug',
        'utilities_common',
        'watchdogutil',
    ],
    package_data={
        'show': ['aliases.ini'],
        'sonic_installer': ['aliases.ini'],
        'tests': ['acl_input/*',
                  'mock_tables/*.py',
                  'mock_tables/*.json',
                  'mock_tables/asic0/*.json',
                  'mock_tables/asic1/*.json',
                  'filter_fdb_input/*',
                  'pfcwd_input/*']
    },
    scripts=[
        'scripts/aclshow',
        'scripts/asic_config_check',
        'scripts/boot_part',
        'scripts/coredump-compress',
        'scripts/configlet',
        'scripts/db_migrator.py',
        'scripts/decode-syseeprom',
        'scripts/dropcheck',
        'scripts/dropconfig',
        'scripts/dropstat',
        'scripts/dump_nat_entries.py',
        'scripts/ecnconfig',
        'scripts/fanshow',
        'scripts/fast-reboot',
        'scripts/fast-reboot-dump.py',
        'scripts/fdbclear',
        'scripts/fdbshow',
        'scripts/gearboxutil',
        'scripts/generate_dump',
        'scripts/intfutil',
        'scripts/intfstat',
        'scripts/lldpshow',
        'scripts/log_ssd_health',
        'scripts/mellanox_buffer_migrator.py',
        'scripts/mmuconfig',
        'scripts/natclear',
        'scripts/natconfig',
        'scripts/natshow',
        'scripts/nbrshow',
        'scripts/neighbor_advertiser',
        'scripts/pcmping',
        'scripts/port2alias',
        'scripts/portconfig',
        'scripts/portstat',
        'scripts/pfcstat',
        'scripts/psushow',
        'scripts/queuestat',
        'scripts/reboot',
        'scripts/route_check.py',
        'scripts/route_check_test.sh',
        'scripts/sfpshow',
        'scripts/syseeprom-to-json',
        'scripts/tempershow',
        'scripts/update_json.py',
        'scripts/warm-reboot',
        'scripts/watermarkstat',
        'scripts/watermarkcfg',
        'scripts/sonic-kdump-config'
    ],
    entry_points={
        'console_scripts': [
            'acl-loader = acl_loader.main:cli',
            'config = config.main:config',
            'connect = connect.main:connect',
            'consutil = consutil.main:consutil',
            'counterpoll = counterpoll.main:cli',
            'crm = crm.main:cli',
            'debug = debug.main:cli',
            'filter_fdb_entries = fdbutil.filter_fdb_entries:main',
            'pfcwd = pfcwd.main:cli',
            'sfputil = sfputil.main:cli',
            'ssdutil = ssdutil.main:ssdutil',
            'pfc = pfc.main:cli',
            'psuutil = psuutil.main:cli',
            'fwutil = fwutil.main:cli',
            'pcieutil = pcieutil.main:cli',
            'pddf_fanutil = pddf_fanutil.main:cli',
            'pddf_psuutil = pddf_psuutil.main:cli',
            'pddf_thermalutil = pddf_thermalutil.main:cli',
            'pddf_ledutil = pddf_ledutil.main:cli',
            'show = show.main:cli',
            'sonic-clear = clear.main:cli',
            'sonic-installer = sonic_installer.main:sonic_installer',
            'sonic_installer = sonic_installer.main:sonic_installer',  # Deprecated
            'undebug = undebug.main:cli',
            'watchdogutil = watchdogutil.main:watchdogutil',
        ]
    },
    install_requires=[
        'click',
        'ipaddress',
        'jsondiff==1.2.0',
        'm2crypto',
        'natsort',
        'pexpect',
        'sonic-config-engine',
        'sonic-py-common',
        'swsssdk>=2.0.1',
        'tabulate==0.8.2',
        'xmltodict==0.12.0'
    ],
    setup_requires= [
        'pytest-runner'
    ],
    tests_require = [
        'pytest',
        'mock>=2.0.0',
        'mockredispy>=2.9.3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    keywords='sonic SONiC utilities command line cli CLI',
    test_suite='setup.get_test_suite'
)
