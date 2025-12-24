// Variables to use accross the project
// which can be accessed by var.project_id
variable "project_id" {
  description = "The project ID to host the cluster in"
  default     = "anhnd172-mle-k5"
}

variable "region" {
  description = "The region the cluster in"
  default     = "asia-southeast1"
}

variable "zone" {
  description = "Zone where the instance will be created"
  default     = "asia-southeast1-b"
}

variable "machine_type" {
  description = "Machine type for the Jenkins instance"
  default     = "e2-standard-2"
}
