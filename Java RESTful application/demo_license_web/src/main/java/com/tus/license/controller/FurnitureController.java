package com.tus.license.controller;

import java.util.List;
import java.util.Optional;  //this is required to be able to use "Optional" (a container to store not null object)

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
//import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

//imports of the other packages needed for the REST controllers to operate
import com.tus.license.dto.Furniture;
import com.tus.license.exception.ResourceNotFoundException;
import com.tus.license.repository.FurnitureRepository;


@RestController
public class FurnitureController{
	
	//Annotate with "Autowired"
	@Autowired  //this will create an instance of a FurnitureRepository
	private FurnitureRepository furnRepository;
	
	//this is our default entry into the project
	@GetMapping("/")
	public String index() {
		return "<h2> A00320562 Application </hr>";
	}	
	
	@GetMapping("/Furniture")  //building of our entry path for the project
	public List<Furniture>getFurniture(){
		return furnRepository.findAll();  //will return a list of all Furniture in the DB
	}//end of the get a list of all Furniture's in the DB
	
	
	@GetMapping("/Furniture/id/{id}")  //building of our entry path based on a Long id parameter being passed in the request message
	public ResponseEntity<Furniture>getFurnitureById(@PathVariable(value="id")Long Id)throws ResourceNotFoundException{
		Optional<Furniture>furniture=furnRepository.findById(Id);
		
		if(furniture.isPresent())
			return ResponseEntity.ok().body(furniture.get());
		else
			throw new ResourceNotFoundException("Furniture id not found :: ");
	}//end of get a Furniture by id
	
	@GetMapping("/Furniture/avail/{availability}")  //building of our entry path based on a String availability parameter being passed in the request message
	public ResponseEntity<List<Furniture>> getFurnitureByAvailability(@PathVariable(value = "availability") String availability) throws ResourceNotFoundException {
		List<Furniture> furniture = furnRepository.findByAvailability(availability);

	    if (!furniture.isEmpty())
	        return ResponseEntity.ok().body(furniture);
	    else
			throw new ResourceNotFoundException("Furniture availability not found :: ");
	}//end of get a Furniture by availability
	
	@GetMapping("/Furniture/manu/{manufacturer}")  //building of our entry path based on a String manufacturer parameter being passed in the request message
	public ResponseEntity<List<Furniture>> getFurnitureByManufacturer(@PathVariable(value="manufacturer") String manufacturer) throws ResourceNotFoundException {
		List<Furniture> furniture = furnRepository.findByManufacturer(manufacturer);

	    if (!furniture.isEmpty())
	        return ResponseEntity.ok().body(furniture);
	    else
			throw new ResourceNotFoundException("Furniture manufacturer not found :: ");
	}//end of get a Furniture by manufacture
	
	@GetMapping("/Furniture/type/{productType}")  //building of our entry path based on a String productType parameter being passed in the request message
	public ResponseEntity<List<Furniture>> getFurnitureByProductType(@PathVariable(value="productType") String productType) throws ResourceNotFoundException {
		List<Furniture>furniture = furnRepository.findByProductType(productType);

	    if (!furniture.isEmpty())
	        return ResponseEntity.ok().body(furniture);
	    else
			throw new ResourceNotFoundException("Furniture productType not found :: ");
	}//end of get a Furniture by productType

	@GetMapping("/Furniture/type/{productType}/{furnitureType}")  //building of our entry path based on a String product and furniture parameter being passed in the request message
	public ResponseEntity<List<Furniture>> getFurnitureByProductTypeAndType(@PathVariable(value="productType") String productType,
																		@PathVariable(value="furnitureType") String furnitureType) throws ResourceNotFoundException {
		List<Furniture>furniture = furnRepository.findByProductTypeAndFurnitureType(productType,furnitureType);

	    if (!furniture.isEmpty())
	        return ResponseEntity.ok().body(furniture);
	    else
			throw new ResourceNotFoundException("Furniture productType and FurnitureType not found :: ");
	}//end of get a Furniture by productType and FurnitureType
	
	
	@PostMapping("/Furniture/")  //building of our entry path to add an Entity to the database
	public Furniture createFurniture(@RequestBody Furniture furnitureData) {
		return furnRepository.save(furnitureData);
	}//end of the POST create a Furniture entity

	
	@DeleteMapping("/Furniture/{id}")
	public void deleteFurniture(@PathVariable(value="id")Long furnitureId) {
		furnRepository.deleteById(furnitureId);
	}
	
	@DeleteMapping("/Furniture/type/{productType}")
	public void deleteFurnitureByType(@PathVariable(value="productType") String productType) {
	    furnRepository.deleteByProductType(productType);
	}
	
	@DeleteMapping("/Furniture/manu/{manufacturer}")
	public void deleteFurnitureByManufacturer(@PathVariable(value="manufacturer") String manufacturer) {
	    furnRepository.deleteByManufacturer(manufacturer);
	}
	
	@DeleteMapping("/Furniture/avail/{availability}")
	public void deleteFurnitureByAvailability(@PathVariable(value="availability") String availability) {
	    furnRepository.deleteByAvailability(availability);
	}
	
	
}//end of FurnitureController class

