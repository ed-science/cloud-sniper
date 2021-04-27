module "base" {
    source = "../modules/base"
}

module "iam" {
  source = "../modules/iam"
}

module "threat-intelligence" {
  source = "../modules/threat-intelligence"
}

module "dashboard" {
  source = "../modules/dashboard"

  ssh_key_name="blbalbalblab"
  vpc_id="blbalbalblab"
  bucket_name="blbalbalblab"
  subnet_id="blbalbalblab"
}