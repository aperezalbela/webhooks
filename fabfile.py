from fabric.api import sudo, hosts

@hosts('intranet.scrapinghub.com')
def deploy():
    sudo("apt-get -qq update && apt-get -qy install --only-upgrade hubsite")
