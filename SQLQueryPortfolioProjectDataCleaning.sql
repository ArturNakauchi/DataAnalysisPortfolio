/*

Cleaning Data in SQL Queries

*/

SELECT *
FROM CleaningDataPortfolioProject.dbo.NashvilleHousing

----------------------------------------------------------------------------------------------
-- Standardize Date Formats

SELECT SaleDate, CONVERT(Date, SaleDate)
FROM CleaningDataPortfolioProject.dbo.NashvilleHousing

--ALTER TABLE NashvilleHousing
--ADD SaleDateConverted Date;

--UPDATE NashvilleHousing
--SET SaleDateConverted = CONVERT(Date, SaleDate)

SELECT SaleDateConverted, CONVERT(Date, SaleDate)
FROM CleaningDataPortfolioProject.dbo.NashvilleHousing
ORDER BY SaleDate DESC

---------------------------------------------------------------------------------------------
-- Populate Property Adress Data

-- ParcelIDs contain the address that would fill in the Property Adress Data
SELECT *
FROM CleaningDataPortfolioProject..NashvilleHousing
--WHERE PropertyAddress is null
ORDER BY ParcelID	

-- Compare two columns with JOIN, check if the columns have different unique IDs with "<>" and check if the property address on A is null
-- Make a new column with the results
-- This SELECT query should be empty when the results are fixed
--  Update the database with the above using SET
SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM CleaningDataPortfolioProject..NashvilleHousing a
JOIN CleaningDataPortfolioProject..NashvilleHousing b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b. [UniqueID ]
WHERE a.PropertyAddress is null


UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM CleaningDataPortfolioProject..NashvilleHousing a
JOIN CleaningDataPortfolioProject..NashvilleHousing b
	ON a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b. [UniqueID ]
WHERE a.PropertyAddress is null

---------------------------------------------------------------------------------------
-- Breaking out Address into Individual columns (Address, City ,State)

SELECT PropertyAddress
FROM CleaningDataPortfolioProject..NashvilleHousing
--WHERE PropertyAddress is null
--ORDER BY ParcelID	


SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) - 1 ) AS Address
, SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress))AS Address

FROM CleaningDataPortfolioProject..NashvilleHousing


--ALTER TABLE NashvilleHousing
--ADD PropertySplitAddress nvarchar(255);

--ALTER TABLE NashvilleHousing
--ADD PropertySplitCity nvarchar(255);

--UPDATE NashvilleHousing
--SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) - 1 )

--UPDATE NashvilleHousing
--SET PropertySplitCity =  SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress))

SELECT *
FROM CleaningDataPortfolioProject..NashvilleHousing


SELECT OwnerAddress
FROM CleaningDataPortfolioProject..NashvilleHousing

--Using PARSENAME + REPLACE to look for the commas and split the columns (Easy way) Does it backwards for some reason

SELECT
PARSENAME(REPLACE(OwnerAddress, ',' , '.'), 3)
, PARSENAME(REPLACE(OwnerAddress, ',' , '.'), 2)
, PARSENAME(REPLACE(OwnerAddress, ',' , '.'), 1)
FROM CleaningDataPortfolioProject..NashvilleHousing

ALTER TABLE NashvilleHousing
ADD OwnerSplitAddress nvarchar(255);

ALTER TABLE NashvilleHousing
ADD OwnerSplitCity nvarchar(255);

ALTER TABLE NashvilleHousing
ADD OwnerSplitState nvarchar(255);

UPDATE NashvilleHousing
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',' , '.'), 3)

UPDATE NashvilleHousing
SET OwnerSplitCity =  PARSENAME(REPLACE(OwnerAddress, ',' , '.'), 2)

UPDATE NashvilleHousing
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',' , '.'), 1)


------------------------------------------------------------------------------------

--Change Y and N to Yes and No in "Sold as Vacant" field

SELECT DISTINCT(SoldAsVacant), COUNT(SoldAsVacant)
FROM CleaningDataPortfolioProject..NashvilleHousing
GROUP BY SoldAsVacant
ORDER BY 2


SELECT SoldAsVacant
, CASE WHEN SoldASVacant = 'Y' THEN 'Yes'
	   WHEN SoldASVacant = 'N' THEN 'No'
	   ELSE SoldASVacant 
	   END
FROM CleaningDataPortfolioProject..NashvilleHousing

UPDATE NashvilleHousing
SET SoldAsVacant = CASE WHEN SoldASVacant = 'Y' THEN 'Yes'
	   WHEN SoldASVacant = 'N' THEN 'No'
	   ELSE SoldASVacant 
	   END

--------------------------------------------------------------------------

-- Remove Duplicates with different UniqueIDs using a CTE

WITH RowNumCTE AS(
Select *,
	ROW_NUMBER() OVER (
	PARTITION BY ParcelID,
				 PropertyAddress,
				 SalePrice,
				 SaleDate,
				 LegalReference
				 ORDER BY
					UniqueID
					) row_num

FROM CleaningDataPortfolioProject..NashvilleHousing
)
---- Deleting the duplicates
--DELETE
--FROM RowNumCTE
--WHERE row_num > 1
SELECT *
FROM RowNumCTE
WHERE row_num > 1
Order BY PropertyAddress

---------------------------------------------------------------------

-- Delete unused columns

SELECT *
FROM CleaningDataPortfolioProject..NashvilleHousing

ALTER TABLE CleaningDataPortfolioProject..NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate