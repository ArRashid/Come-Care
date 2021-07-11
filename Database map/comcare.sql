-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 11, 2021 at 06:34 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `comcare`
--

-- --------------------------------------------------------

--
-- Table structure for table `contract`
--

CREATE TABLE `contract` (
  `sn` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `msg` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contract`
--

INSERT INTO `contract` (`sn`, `name`, `email`, `phone`, `msg`) VALUES
(6646447, 'lllllllllllllllll', 'asdaskd@gmai.com', '1212121212', 'adjahdsjkashdaSASkahsdjdfsfdasdasdksdajkljdlk'),
(6646448, 'ar', 'ar@gmail.com', '2147483647', 'sakjdkasljdl'),
(6646449, 'ar', 'ar@gmail.com', '2147483647', 'sakjdkasljdldasd'),
(6646450, 'xxxxxxxxxxxx', 'ar@gmail.com', '2147483647', 'sakjdkasljdldasda'),
(6646451, 'xxxxxxxxxxxx', 'ar@gmail.com', '2147483647', 'sakjdkasljdldasda'),
(6646452, 'lsajdaklsdj', 'aksljdlakj@gmail.com', '8888888888', 'asdjaskldjklsajdklasd'),
(6646453, 'lsajdaklsdj', 'aksljdlakj@gmail.com', '9999999999', 'asdjaskldjklsajdklasd'),
(6646454, 'lsajdaklsdj', 'aksljdlakj@gmail.com', '4555555555', 'asdjaskldjklsajdklasd'),
(6646455, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646456, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646457, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646458, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646459, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646460, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646461, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646462, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646463, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646464, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646465, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646466, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646467, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646468, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646469, 'khan sir', 'khan@gmail.com', '7878787877', 'this massage from khan'),
(6646470, 'khan sir 2', 'kh5an@gmail.com', '7878187877', 'this massage from khan'),
(6646471, 'ghfhf', 'ddfgfd@gg.voo', 'ffgfgh', 'ggfghfgh');

-- --------------------------------------------------------

--
-- Table structure for table `emp`
--

CREATE TABLE `emp` (
  `emp_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `pf` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `bio` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(20) NOT NULL,
  `pin` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `dist` varchar(20) NOT NULL,
  `field` varchar(20) NOT NULL,
  `ql` varchar(255) NOT NULL,
  `cer` varchar(1000) NOT NULL,
  `exp` varchar(255) DEFAULT NULL,
  `adhar_no` varchar(20) NOT NULL,
  `adhar_sc` varchar(255) NOT NULL,
  `msg` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emp`
--

INSERT INTO `emp` (`emp_id`, `name`, `pf`, `phone`, `email`, `bio`, `address`, `city`, `pin`, `state`, `dist`, `field`, `ql`, `cer`, `exp`, `adhar_no`, `adhar_sc`, `msg`) VALUES
(74, 'Mr TT jack', 'static\\uploads\\emp\\profile\\Mr_TT_jack_profile_istockphoto-1130014022-612x612.jpg', '9133531223', 'jCK@gmail.com', 'I am a c enge', 'askjdhjkasjdhjakd', 'Amtona', '7465656', 'West Bengal', 'North 24 Parganas', '1', 'Plambers', ',static\\uploads\\emp\\proofs\\Mr_TT_jack_proof_jCKgmail.comScreenshot_1.png,static\\uploads\\emp\\proofs\\Mr_TT_jack_proof_jCKgmail.comScreenshot_2.png,static\\uploads\\emp\\proofs\\Mr_TT_jack_proof_jCKgmail.comScreenshot_3.png', '', '35445455564545654', 'static\\uploads\\emp\\\\adhar\\Mr_TT_jack_adhar_card_cv.png', ''),
(75, 'Alita Bruetal', 'static\\uploads\\emp\\profile\\Alita_Bruetal_profile_istockphoto-1135716959-612x612.jpg', '84545454545', 'alital@email.com', 'i an secologist', 'jajsdja', 'Barasat', '7465656', 'West Bengal', 'North 24 Parganas', '2', 'maskdjklasjd', ',static\\uploads\\emp\\proofs\\Alita_Bruetal_proof_alitalemail.comScreenshot_1.png', '', '5456545456', 'static\\uploads\\emp\\\\adhar\\Alita_Bruetal_adhar_card_32c1bd02-4081-4403-93d4-0a892ef7801d.jpg', 'please aprove me'),
(76, 'Alita Bruetal', 'static\\uploads\\emp\\profile\\Alita_Bruetal_profile_istockphoto-1135716959-612x612.jpg', '84545454545', 'alital@email.com', 'i an secologist', 'jajsdja', 'Barasat', '7465656', 'West Bengal', 'North 24 Parganas', '2', 'maskdjklasjd', ',static\\uploads\\emp\\proofs\\Alita_Bruetal_proof_alitalemail.comScreenshot_1.png', '', '5456545456', 'static\\uploads\\emp\\\\adhar\\Alita_Bruetal_adhar_card_32c1bd02-4081-4403-93d4-0a892ef7801d.jpg', 'please aprove me'),
(77, 'Chacha Barkat', 'static\\uploads\\emp\\profile\\Chacha_Barkat_profile_face-of-an-old-man-1431724.jpg', '84545454545', 'alital@email.com', 'i an secologist', 'jajsdja', 'Barasat', '7465656', 'West Bengal', 'North 24 Parganas', '2', 'maskdjklasjd', ',static\\uploads\\emp\\proofs\\Chacha_Barkat_proof_alitalemail.comScreenshot_1.png', '', '5456545456', 'static\\uploads\\emp\\\\adhar\\Chacha_Barkat_adhar_card_32c1bd02-4081-4403-93d4-0a892ef7801d.jpg', 'please aprove me'),
(78, 'Mr TT jack', 'static\\uploads\\emp\\profile\\Mr_TT_jack_profile_istockphoto-1130014022-612x612.jpg', '9133531223', 'jCK@gmail.com', 'I am a c enge', 'askjdhjkasjdhjakd', 'Amtona', '7465656', 'West Bengal', 'North 24 Parganas', '1', 'Plambers', ',static\\uploads\\emp\\proofs\\Mr_TT_jack_proof_jCKgmail.comScreenshot_1.png,static\\uploads\\emp\\proofs\\Mr_TT_jack_proof_jCKgmail.comScreenshot_2.png,static\\uploads\\emp\\proofs\\Mr_TT_jack_proof_jCKgmail.comScreenshot_3.png', '', '35445455564545654', 'static\\uploads\\emp\\\\adhar\\Mr_TT_jack_adhar_card_cv.png', ''),
(79, 'Toykiya Brush', 'static\\uploads\\emp\\profile\\Toykiya_Brush_profile_istockphoto-166226979-612x612.jpg', '9133531223', 'jCK@gmail.com', 'I am a c enge', 'askjdhjkasjdhjakd', 'Amtona', '7465656', 'West Bengal', 'North 24 Parganas', '1', 'Plambers', ',static\\uploads\\emp\\proofs\\Toykiya_Brush_proof_jCKgmail.comScreenshot_1.png,static\\uploads\\emp\\proofs\\Toykiya_Brush_proof_jCKgmail.comScreenshot_2.png,static\\uploads\\emp\\proofs\\Toykiya_Brush_proof_jCKgmail.comScreenshot_3.png', '', '35445455564545654', 'static\\uploads\\emp\\\\adhar\\Toykiya_Brush_adhar_card_cv.png', ''),
(80, 'Lolpa Guppa', 'static\\uploads\\emp\\profile\\Lolpa_Guppa_profile_istockphoto-1080415396-612x612.jpg', '9133531223', 'jCK@gmail.com', 'I am a c enge', 'askjdhjkasjdhjakd', 'Amtona', '7465656', 'West Bengal', 'North 24 Parganas', '1', 'Plambers', ',static\\uploads\\emp\\proofs\\Lolpa_Guppa_proof_jCKgmail.comScreenshot_1.png,static\\uploads\\emp\\proofs\\Lolpa_Guppa_proof_jCKgmail.comScreenshot_2.png,static\\uploads\\emp\\proofs\\Lolpa_Guppa_proof_jCKgmail.comScreenshot_3.png', '', '35445455564545654', 'static\\uploads\\emp\\\\adhar\\Lolpa_Guppa_adhar_card_cv.png', ''),
(81, 'MS Lopar', 'static\\uploads\\emp\\profile\\MS_Lopar_profile_an-old-man-1435337.jpg', '9133531223', 'jCK@gmail.com', 'I am a c enge', 'askjdhjkasjdhjakd', 'Amtona', '7465656', 'West Bengal', 'North 24 Parganas', '1', 'Plambers', ',static\\uploads\\emp\\proofs\\MS_Lopar_proof_jCKgmail.comScreenshot_1.png,static\\uploads\\emp\\proofs\\MS_Lopar_proof_jCKgmail.comScreenshot_2.png,static\\uploads\\emp\\proofs\\MS_Lopar_proof_jCKgmail.comScreenshot_3.png', '', '35445455564545654', 'static\\uploads\\emp\\\\adhar\\MS_Lopar_adhar_card_cv.png', ''),
(82, 'MS Lopar', 'static\\uploads\\emp\\profile\\MS_Lopar_profile_an-old-man-1435337.jpg', '9133531223', 'jCK@gmail.com', 'I am a c enge', 'askjdhjkasjdhjakd', 'Amtona', '7465656', 'West Bengal', 'North 24 Parganas', '1', 'Plambers', ',static\\uploads\\emp\\proofs\\MS_Lopar_proof_jCKgmail.comScreenshot_1.png,static\\uploads\\emp\\proofs\\MS_Lopar_proof_jCKgmail.comScreenshot_2.png,static\\uploads\\emp\\proofs\\MS_Lopar_proof_jCKgmail.comScreenshot_3.png', '', '35445455564545654', 'static\\uploads\\emp\\\\adhar\\MS_Lopar_adhar_card_cv.png', ''),
(83, 'MS Lopar', 'static\\uploads\\emp\\profile\\MS_Lopar_profile_32c1bd02-4081-4403-93d4-0a892ef7801d.jpg', '9133531223', 'jCK@gmail.com', 'I am a c enge', 'askjdhjkasjdhjakd', 'Amtona', '7465656', 'West Bengal', 'North 24 Parganas', '1', 'Plambers', ',static\\uploads\\emp\\proofs\\MS_Lopar_proof_jCKgmail.comScreenshot_1.png,static\\uploads\\emp\\proofs\\MS_Lopar_proof_jCKgmail.comScreenshot_2.png,static\\uploads\\emp\\proofs\\MS_Lopar_proof_jCKgmail.comScreenshot_3.png', '', '35445455564545654', 'static\\uploads\\emp\\\\adhar\\MS_Lopar_adhar_card_cv.png', ''),
(84, 'kljasdjaksl', 'static\\uploads\\emp\\profile\\kljasdjaksl_profile_Screenshot_3.png', '85454545', 'aas@gmai.com', 'kasljdkaslkjd', 'asdhasjkdka', 'a', '743412', 'West Bengal', 'Alipurduar', '1', 'asdasd', ',static\\uploads\\emp\\proofs\\kljasdjaksl_proof_aasgmai.comScreenshot_1.png', '', '45454654654', 'static\\uploads\\emp\\\\adhar\\kljasdjaksl_adhar_card_cv.png', ''),
(85, 'Abdur Rashid Mondal', 'static\\uploads\\emp\\profile\\Abdur_Rashid_Mondal_profile_logo12.gif', '08159030930', 'ar.rashid.mondal@gma', 'I am an Ideot', 'nalkora', 'Basirhat', '743412', 'West Bengal', 'North 24 Parganas', 'Network Engee', 'CCNA', ',static\\uploads\\emp\\proofs\\Abdur_Rashid_Mondal_proof_ar.rashid.mondalgmail.comfavicon.ico', 'nasd', '12121545454', 'static\\uploads\\emp\\\\adhar\\Abdur_Rashid_Mondal_adhar_card_cat_3.gif', '');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `time` datetime DEFAULT current_timestamp(),
  `name` text NOT NULL,
  `address` text NOT NULL,
  `pin` int(11) NOT NULL,
  `dist` varchar(20) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`time`, `name`, `address`, `pin`, `dist`, `phone`, `email`, `password`) VALUES
('2021-06-25 19:47:47', 'Akash Khan', 'Vill Nakora', 743412, 'North 24 Parganas', '8159030930', 'aakash@a.com', 'a'),
('2021-06-27 13:51:57', 'imran mondal', 'amtona ', 156513123, 'North 24 Parganas', '2538355527', 'imranirfanraiyan@gmail.com', 'imranirfan786');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contract`
--
ALTER TABLE `contract`
  ADD PRIMARY KEY (`sn`);

--
-- Indexes for table `emp`
--
ALTER TABLE `emp`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contract`
--
ALTER TABLE `contract`
  MODIFY `sn` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6646472;

--
-- AUTO_INCREMENT for table `emp`
--
ALTER TABLE `emp`
  MODIFY `emp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
