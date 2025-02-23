
# AWS EC2 Instance Type
variable "instance_type" {
  description = "EC2 Instance Type"
  type = string
  default = "t3.micro"  
}

# AWS EC2 Instance Key Pair
variable "instance_keypair" {
  description = "AWS EC2 Key pair that need to be associated with EC2 Instance"
  type = string
  default = "Terraform-key1"
}

# AWS EC2 private instance count
variable "private_instance_count" {
    description = "AWS EC2 Private instances count"
    type = number
    default = 1
  
}