SQLite format 3   @                                                                     .K�� D ��D�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ��tableraterateCREATE TABLE rate (
	user_id INTEGER NOT NULL, 
	restaurant_id INTEGER NOT NULL, 
	value INTEGER NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (user_id, restaurant_id), 
	FOREIGN KEY(user_id) REFERENCES user (id) ON DELETE CASCADE, 
	FOREIGN KEY(restaurant_id) REFERENCES restaurant (id) ON DELETE CASCADE
)'; indexsqlite_autoindex_rate_1rate�O!!�itablerestaurantrestaurantCREATE TABLE restaurant (
	name VARCHAR NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name)
)3G! indexsqlite_autoindex_restaurant_1restaurant�=�]tableuseruserCREATE TABLE user (
	name VARCHAR NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name)
)'; indexsqlite_autoindex_user_1user          � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       < AAJun2023-05-29 03:53:19.8380922023-05-29 03:53:19.838095= AAmasa2023-05-29 03:51:01.5177672023-05-29 03:51:01.517770
   � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Jun	masa   � �u2��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   A AAAmerican2023-05-29 06:06:39.5145832023-05-29 06:06:39.514586H+ AAマハラジャ2023-05-29 06:06:21.2393642023-05-29 06:06:21.239368A AAJapanese2023-05-29 06:06:05.5028612023-05-29 06:06:05.502864B AAかつや2023-05-29 05:05:40.3773782023-05-29 05:05:40.377381E% AAボンルパ2023-05-29 03:51:05.4993862023-05-29 03:51:05.499389
   � �����                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  American+マハラジャJapaneseかつや%	ボンルパ   G ��D��G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 > AA2023-05-29 06:06:58.0321372023-05-29 06:06:58.032139=	 AA2023-05-29 06:06:39.7505852023-05-29 06:06:39.750589=	 AA2023-05-29 06:06:21.6061422023-05-29 06:06:21.606144=	 AA2023-05-29 06:06:05.7454792023-05-29 06:06:05.745482=	 AA2023-05-29 05:05:40.5882232023-05-29 05:05:40.588226=	 AA2023-05-29 03:53:25.9399052023-05-29 03:53:25.939907<		 AA2023-05-29 03:51:05.7635162023-05-29 03:51:27.375681
   � �������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         							