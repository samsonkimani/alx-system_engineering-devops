#creating a pupper script to ensure to create config file and append data
file {'/home/samson/.ssh/config':
  ensure  => present,
  content => '
	Host *
		IdentityFile ~/.ssh/school
		PasswordAuthentication no
	',
}
