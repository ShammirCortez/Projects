package com.tus.license.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.NOT_FOUND)
public class ResourceNotFoundException extends Exception {
	public ResourceNotFoundException(String message) {
		//Because it extends exception we use the super()
		super(message);
	}
}//end of class


