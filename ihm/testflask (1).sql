-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 17 mai 2023 à 00:10
-- Version du serveur : 10.4.27-MariaDB
-- Version de PHP : 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `testflask`
--

-- --------------------------------------------------------

--
-- Structure de la table `brand`
--

CREATE TABLE `brand` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `id_subcategory` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `brand`
--

INSERT INTO `brand` (`id`, `name`, `id_subcategory`) VALUES
(2, 'Apple', 1),
(3, 'Huawei', 1),
(4, 'Oppo', 1),
(5, 'Samsung', 1),
(6, 'Xiaomi', 1);

-- --------------------------------------------------------

--
-- Structure de la table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
(1, 'telephony');

-- --------------------------------------------------------

--
-- Structure de la table `company`
--

CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `link` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `company`
--

INSERT INTO `company` (`id`, `name`, `link`) VALUES
(2, 'tunisanet', 'https://www.tunisianet.com.tn/');

-- --------------------------------------------------------

--
-- Structure de la table `model`
--

CREATE TABLE `model` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `id_marque` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `model`
--

INSERT INTO `model` (`id`, `name`, `id_marque`) VALUES
(2, 'Iphone 11', 2),
(3, 'Iphone 14 pro max', 2),
(5, 'Iphone 12', 2),
(6, 'Nova 10 SE', 3),
(7, 'Nova Y61', 3),
(8, 'Nova Y90', 3),
(9, 'A77S', 4),
(10, 'Reno 8T', 4),
(11, 'A17', 4),
(12, 'Find X5', 4),
(13, 'Galaxy A53', 5),
(14, 'Galaxy A04', 5),
(15, 'Galaxy A04E', 5),
(16, 'Galaxy A04S', 5),
(17, 'Galaxy A23', 5),
(18, 'Redmi 10', 6),
(19, 'Redmi A1', 6),
(20, 'Redmi note 12', 6);

-- --------------------------------------------------------

--
-- Structure de la table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `color` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `storage` int(11) NOT NULL,
  `ram` int(11) NOT NULL,
  `image` varchar(255) NOT NULL,
  `id_model` int(11) NOT NULL,
  `id_company` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `product`
--

INSERT INTO `product` (`id`, `name`, `color`, `price`, `storage`, `ram`, `image`, `id_model`, `id_company`) VALUES
(3, 'Apple Iphone 11', 'Black', 2400, 128, 4, '1684159040.jpg', 2, 2),
(4, 'Apple Iphone 14 pro max', 'Black', 8600, 512, 6, '1684159298.jpg', 3, 2),
(5, 'Apple Iphone 14 pro max', 'Deep Purple', 7380, 256, 6, '1684159359.jpg', 3, 2),
(6, 'Apple Iphone 12', 'White', 3300, 64, 4, '1684159560.jpg', 5, 2),
(7, 'Apple Iphone 14 pro max', 'Gold', 7380, 256, 6, '1684159608.jpg', 3, 2),
(8, 'Huawei Nova 10 SE', 'Grey', 1600, 256, 8, '1684159689.jpg', 6, 2),
(9, 'Huawei Nova Y61', 'Black', 700, 64, 4, '1684159768.jpg', 7, 2),
(10, 'Huawei Nova Y90', 'Blue', 1070, 128, 6, '1684160069.jpg', 8, 2),
(11, 'Oppo A77S', 'Blue', 935, 128, 8, '1684160695.jpg', 9, 2),
(12, 'Oppo Reno 8T', 'Orange', 1380, 256, 8, '1684160758.jpg', 10, 2),
(13, 'Oppo Reno 8T', 'Gold', 1380, 256, 8, '1684160792.jpg', 10, 2),
(14, 'Oppo A17', 'Blue', 575, 64, 3, '1684160865.jpg', 11, 2),
(15, 'Samsung Galaxy A53', 'Black', 1960, 128, 8, '1684161846.jpg', 13, 2),
(16, 'Samsung Galaxy A04', 'White', 550, 64, 4, '1684161914.jpg', 14, 2),
(17, 'Samsung Galaxy A04E', 'Blue', 500, 32, 4, '1684162186.jpg', 15, 2),
(19, 'Samsung Galaxy A04S', 'Black', 680, 64, 4, '1684162355.jpg', 16, 2),
(20, 'Samsung Galaxy A23', 'White', 660, 64, 4, '1684162401.jpg', 17, 2),
(21, 'Xiaomi Redmi 10', 'White', 780, 128, 6, '1684162580.jpg', 18, 2),
(22, 'Xiaomi Redmi A1', 'Black', 350, 32, 2, '1684162719.jpg', 19, 2),
(23, 'Xiaomi Redmi note 12', 'Blue', 770, 128, 4, '1684162764.jpg', 20, 2),
(24, 'Xiaomi Redmi note 12', 'Black', 770, 128, 4, '1684162785.jpg', 20, 2),
(25, 'Oppo Find X5', 'Black', 3500, 256, 6, '1684162892.jpg', 12, 2);

-- --------------------------------------------------------

--
-- Structure de la table `profile`
--

CREATE TABLE `profile` (
  `id` int(11) NOT NULL,
  `login` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `profile`
--

INSERT INTO `profile` (`id`, `login`, `password`) VALUES
(3, 'ketatasalem7@gmail.com', 'salem123'),
(4, 'dhouibhana32@gmail.com', 'Hana123'),
(6, 'mounafgaier@gmail.com', 'Mouna123');

-- --------------------------------------------------------

--
-- Structure de la table `rate`
--

CREATE TABLE `rate` (
  `id` int(11) NOT NULL,
  `id_product` int(11) NOT NULL,
  `id_customer` int(11) NOT NULL,
  `score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `rate`
--

INSERT INTO `rate` (`id`, `id_product`, `id_customer`, `score`) VALUES
(1, 6, 2, 2),
(2, 3, 2, 3),
(3, 3, 2, 5),
(4, 3, 2, 3),
(5, 3, 2, 4),
(6, 3, 2, 3),
(7, 3, 2, 3),
(8, 3, 2, 3),
(9, 3, 2, 5),
(10, 3, 2, 2),
(11, 3, 2, 4),
(12, 3, 2, 5),
(13, 3, 2, 5),
(14, 3, 2, 5);

-- --------------------------------------------------------

--
-- Structure de la table `subcategory`
--

CREATE TABLE `subcategory` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `id_category` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `subcategory`
--

INSERT INTO `subcategory` (`id`, `name`, `id_category`) VALUES
(1, 'smartphone', 1);

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `postalcode` int(11) NOT NULL,
  `birthdate` date NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `childnumber` int(11) NOT NULL,
  `civilstate` varchar(50) NOT NULL,
  `id_profile` int(11) NOT NULL,
  `role` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id`, `name`, `address`, `postalcode`, `birthdate`, `email`, `phone`, `city`, `gender`, `childnumber`, `civilstate`, `id_profile`, `role`) VALUES
(1, 'salem ketata', 'Mharza km 3', 3052, '1999-10-07', 'ketatasalem7@gmail.com', '94176012', 'sfax', 'male', 2, 'married', 3, 'admin'),
(2, 'Hana Dhouib', 'Route Tounes km 5.5', 3011, '2000-02-20', 'dhouibhana32@gmail.com', '25182999', 'sfax', 'female', 2, 'Married', 4, 'customer'),
(4, 'Mouna Fgaier', 'Route Sokra km 4', 3052, '1998-11-20', 'mounafgaier@gmail.com', '94176012', 'Sfax', 'female', 0, 'Single', 6, 'customer');

-- --------------------------------------------------------

--
-- Structure de la table `validation`
--

CREATE TABLE `validation` (
  `id` int(11) NOT NULL,
  `id_product` int(11) NOT NULL,
  `id_customer` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `validation`
--

INSERT INTO `validation` (`id`, `id_product`, `id_customer`) VALUES
(1, 3, 2),
(2, 6, 2),
(3, 5, 2),
(4, 3, 2),
(5, 3, 2),
(6, 3, 2),
(7, 3, 2);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`id`),
  ADD KEY `forgeinkey_subcategory` (`id_subcategory`);

--
-- Index pour la table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `model`
--
ALTER TABLE `model`
  ADD PRIMARY KEY (`id`),
  ADD KEY `forgeinkey_marque` (`id_marque`);

--
-- Index pour la table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `forgeinkey_model` (`id_model`),
  ADD KEY `forgeinkey_company` (`id_company`);

--
-- Index pour la table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `rate`
--
ALTER TABLE `rate`
  ADD PRIMARY KEY (`id`),
  ADD KEY `forgeinkey_product` (`id_product`),
  ADD KEY `forgeinkey_customer` (`id_customer`);

--
-- Index pour la table `subcategory`
--
ALTER TABLE `subcategory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `forgeinkey_category` (`id_category`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD KEY `forgeinkey_profil` (`id_profile`);

--
-- Index pour la table `validation`
--
ALTER TABLE `validation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `forgeinkeyval_product` (`id_product`),
  ADD KEY `forgeinkeyval_customer` (`id_customer`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `brand`
--
ALTER TABLE `brand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `company`
--
ALTER TABLE `company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `model`
--
ALTER TABLE `model`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT pour la table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT pour la table `profile`
--
ALTER TABLE `profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `rate`
--
ALTER TABLE `rate`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT pour la table `subcategory`
--
ALTER TABLE `subcategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `validation`
--
ALTER TABLE `validation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `brand`
--
ALTER TABLE `brand`
  ADD CONSTRAINT `forgeinkey_subcategory` FOREIGN KEY (`id_subcategory`) REFERENCES `subcategory` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `model`
--
ALTER TABLE `model`
  ADD CONSTRAINT `forgeinkey_marque` FOREIGN KEY (`id_marque`) REFERENCES `brand` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `forgeinkey_company` FOREIGN KEY (`id_company`) REFERENCES `company` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `forgeinkey_model` FOREIGN KEY (`id_model`) REFERENCES `model` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `rate`
--
ALTER TABLE `rate`
  ADD CONSTRAINT `forgeinkey_customer` FOREIGN KEY (`id_customer`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `forgeinkey_product` FOREIGN KEY (`id_product`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `subcategory`
--
ALTER TABLE `subcategory`
  ADD CONSTRAINT `forgeinkey_category` FOREIGN KEY (`id_category`) REFERENCES `category` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `forgeinkey_profil` FOREIGN KEY (`id_profile`) REFERENCES `profile` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `validation`
--
ALTER TABLE `validation`
  ADD CONSTRAINT `forgeinkeyval_customer` FOREIGN KEY (`id_customer`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `forgeinkeyval_product` FOREIGN KEY (`id_product`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
