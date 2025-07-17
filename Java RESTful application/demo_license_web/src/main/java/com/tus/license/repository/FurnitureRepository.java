package com.tus.license.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

//import the other packages needed here
import com.tus.license.dto.Furniture;
import java.util.List;
import org.springframework.data.jpa.repository.Modifying;

@Repository
public interface FurnitureRepository extends JpaRepository<Furniture, Long>{
	
	List<Furniture> findByAvailability(String availability);	
	List<Furniture> findByManufacturer(String manufacturer);
	List<Furniture> findByProductType(String productType);
	List<Furniture> findByProductTypeAndFurnitureType(String productType, String furnitureType);
	
	@Modifying
	@Transactional
	void deleteByProductType(String productType);
	
	@Modifying
	@Transactional
	void deleteByManufacturer(String manufacturer);
	
	@Modifying
	@Transactional
	void deleteByAvailability(String availability);

}


