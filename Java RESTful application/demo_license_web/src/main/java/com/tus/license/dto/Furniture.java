package com.tus.license.dto;

import javax.persistence.*;  //import the entire library


@Entity
//Specify the name of the table that it is mapped to
@Table(name = "LICENSE")
public class Furniture {
	
	//declaring the various variables then Annotate each to map to the new Table LICENSE
	
	@Id //	THIS SETS THE PRIMARY KEY
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(name = "ID") //Specify the column name for mapping
	private Long id;
	
	@Column(name = "PRODUCT_ID") //Specify the column name for mapping
	private String productId;
	
	@Column(name = "MANUFACTURER") //Specify the column name for mapping
	private String manufacturer;
	
	@Column(name = "PRODUCT_TYPE") //Specify the column name for mapping
	private String productType;
	
	@Column(name = "FURNITURE_TYPE") //Specify the column name for mapping
	private String furnitureType;
	
	@Column(name = "AVAILABILITY") //Specify the column name for mapping
	private String availability;
	
	
	//constructors
	public Furniture(Long id, String productId, String manufacturer, String productType, String furnitureType,
			String availability) {
		super();
		this.id = id;
		this.productId = productId;
		this.manufacturer = manufacturer;
		this.productType = productType;
		this.furnitureType = furnitureType;
		this.availability = availability;
	}

	public Furniture() {
		//super();
	}
	
	//Getter and Setter methods for all
	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getProductId() {
		return productId;
	}

	public void setProductId(String productId) {
		this.productId = productId;
	}

	public String getManufacturer() {
		return manufacturer;
	}

	public void setManufacturer(String manufacturer) {
		this.manufacturer = manufacturer;
	}

	public String getProductType() {
		return productType;
	}

	public void setProductType(String productType) {
		this.productType = productType;
	}

	public String getFurnitureType() {
		return furnitureType;
	}

	public void setFurnitureType(String furnitureType) {
		this.furnitureType = furnitureType;
	}

	public String getAvailability() {
		return availability;
	}

	public void setAvailability(String availability) {
		this.availability = availability;
	}

	@Override
	public String toString() {
		return "Furniture [id=" + id + ", productId=" + productId + ", manufacturer=" + manufacturer
				+ ", productType=" + productType + ", furnitureType=" + furnitureType + ", availability=" + availability
				+ "]";
	}
} 