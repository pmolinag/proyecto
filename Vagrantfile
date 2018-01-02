require 'vagrant-azure'

Vagrant.configure('2') do |config|

  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box'
  config.vm.network "public_network", ip: "192.168.33.90"
  config.vm.hostname = "localhost"
  config.vm.network :forwarded_port, guest: 80, host: 80
  config.ssh.username = 'vagrant'
  config.ssh.private_key_path = File.expand_path('~/.ssh/id_rsa')

  config.vm.provider :azure do |azure, override|
    # use local ssh key to connect to remote vagrant box
    config.ssh.private_key_path = '/home/pablo/.ssh/id_rsa'
    azure.location = 'eastus'
    azure.tcp_endpoints = '80'
    azure.vm_name = "flyfinder"
    azure.vm_size = 'Standard_DS1_v2'
    azure.resource_group_name = "myResourceGroupAnsible"
    azure.vm_image_urn = 'Canonical:UbuntuServer:16.04-LTS:16.04.201611220'
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
  end

  config.vm.provision "ansible" do |ansible|
    ansible.become = true
    ansible.playbook = "./provision/playbook.yml"
    ansible.verbose = "v"
    ansible.host_key_checking = false
  end

end
