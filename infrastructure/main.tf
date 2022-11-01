terraform {
  required_providers {
    yandex = {
      source = "terraform-registry.storage.yandexcloud.net/yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
 token     = var.token
 cloud_id  = var.cloud_id
 folder_id = var.folder_id
 zone      = "ru-central1-a"
}

resource "yandex_compute_instance" "vm" {
    count = 1
    name = "vm${count.index}"
    resources {
        cores  = 2
        memory = 2
    }

    boot_disk {
        initialize_params {
            image_id = "fd80jfslq61mssea4ejn"
        }
    }

    network_interface {
        subnet_id = "e9bhp1sm4upq328p2jm4"
        nat       = true
    }

    metadata = {
        user-data = file(var.new_user)
    }
  }

output "instance_output" {
  value = [
    for instance in yandex_compute_instance.vm[*] :
    join(": ", [instance.name, instance.hostname, instance.network_interface.0.ip_address, instance.network_interface.0.nat_ip_address])
  ]
}


