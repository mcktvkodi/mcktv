<?php 

$output = "Denied";

// Check for a URL match
if($_SERVER['HTTP_HOST'] == "mcktv.co.uk"){
  $access = 1;

// ... or check for an IP match
} else if($_SERVER['REMOTE_ADDR'] == "127.0.0.1") {
  $access = 1;

} else {
  $access = 0;
}

// If we have access, show output to XML
if ($access == 1):

	// Set the header
	header('Content-Type: application/xml');
	
	// Start output buffering
	ob_start(); 

	// Paste your XML below
	?>

<root>
   <name>sample_name</name>
</root>

    	<?php 
	
	// Collect XML output 
	$output = ob_get_clean( );

endif; 

// print the output. 
print ($output);
