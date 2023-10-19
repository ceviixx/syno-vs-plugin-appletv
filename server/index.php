<?php 
$type = $_GET['type'];
$contentType = '';


$title = $_GET['title'];
$title = str_replace(' ', '+', $title);

$lang = $_GET['lang'];
$langCode = '';
$locale = '';





switch ($type) {
	case "movie":
		$contentType = 'uts.col.search.MV';
		break;
	case "":
		$contentType = 'uts.col.search.SH';
		break;
}


switch ($lang) {
	case "dan":
		$langCode = "";
		break;
	case "ger":
	$langCode = '143443';
		$locale = 'de-DE'; 
		break;
	case "enu":
		$langCode = "";
		break;
	case "spn":
		$langCode = "";
		break;
	case "fre":
		$langCode = "";
		break;
	case "ita":
		$langCode = "";
		break;
	case "hun":
		$langCode = "";
		break;
	case "nld":
		$langCode = "";
		break;
	case "nor":
		$langCode = "";
		break;
	case "plk":
		$langCode = "";
		break;
	case "ptg":
		$langCode = "";
		break;
	case "ptb":
		$langCode = "";
		break;
	case "sve":
		$langCode = "";
		break;
	case "trk":
		$langCode = "";
		break;
	case "csy":
		$langCode = "";
		break;
	case "rus":
		$langCode = "";
		break;
	case "tha":
		$langCode = "";
		break;
	case "jpn":
		$langCode = "";
		break;
	case "chs":
		$langCode = "";
		break;
	case "krn":
		$langCode = "";
		break;
}

$appleTVurl = 'https://uts-api.itunes.apple.com/uts/v2/search/incremental?sf='.$langCode.'&locale='.$locale.'&caller=wta&utsk=0893ae2c4df5b61%3A%3A%3A%3A%3A%3Ac5a7986b1ef4302&v=34&pfm=desktop&q=' . $title;

$jsonData = file_get_contents($appleTVurl);


$json = json_decode($jsonData);
$data = $json->data;
$canvas = $data->canvas;
$shelves = $canvas->shelves;



// FOR SYNO


$synItems = array();

// FOR SYNO

foreach ($shelves as $shelf) {
	if ($shelf->id == $contentType) {
		
		$items = $shelf->items;
		
		foreach ($items as $item) {
			
			if ($item->type != 'MovieBundle') {
				
				
				$itent = $item->id;
				
				$infoURL = 'https://tv.apple.com/api/uts/v2/view/product/'.$itent.'/?utscf=OjAAAAAAAAA~&utsk=000000000000000000&caller=web&sf=143443&v=40&pfm=web&locale=de-DE'; 
				$detailJSONdata = file_get_contents($infoURL);
				$detailJSON = json_decode($detailJSONdata);
				$dC = $detailJSON->data->content;
				$dR = $detailJSON->data->roles;
				$dT = $detailJSON->data->rottenTomatoesReviews;
				
				$rating = $item->rating->displayName;
				
				
				
				
				$genres = array();
				foreach ($dC->genres as $value) {
					$genres[] = $value->name;
				}
				
				
				$actors = array();
				$directors = array();
				$writers = array();
				
				
				
				foreach ($dR as $value) {
					switch ($value->type) {
						case "Actor":
							$actors[] = $value->personName;
							break;
						case "Director":
							$directors[] = $value->personName;
							break;
						case "Producer":
							
							break;
						case "Writer":
							$writers[] = $value->personName;
							break;
					}
				}
				
				
				
				// ARTWORKS
				$coverArt = $dC->images->coverArt;
				$coverArtURL = $coverArt->url;
				$coverArtURL = str_replace('{w}', $coverArt->width, $coverArtURL);
				$coverArtURL = str_replace('{h}', $coverArt->height, $coverArtURL);
				$coverArtURL = str_replace('{f}', 'jpg', $coverArtURL);
				$coverArray = array();
				$coverArray[] = $coverArtURL;
				
				$fullScreenBackground = $dC->images->fullScreenBackground;
				$fullScreenBackgroundURL = $fullScreenBackground->url;
				$fullScreenBackgroundURL = str_replace('{w}', $fullScreenBackground->width, $fullScreenBackgroundURL);
				$fullScreenBackgroundURL = str_replace('{h}', $fullScreenBackground->height, $fullScreenBackgroundURL);
				$fullScreenBackgroundURL = str_replace('{f}', 'jpg', $fullScreenBackgroundURL);
				
				$previewFrame = $dC->images->previewFrame;
				$previewFrameURL = $previewFrame->url;
				$previewFrameURL = str_replace('{w}', $previewFrame->width, $previewFrameURL);
				$previewFrameURL = str_replace('{h}', $previewFrame->height, $previewFrameURL);
				$previewFrameURL = str_replace('{f}', 'jpg', $previewFrameURL);
				
				
				$backdropArray = array();
				if ($fullScreenBackgroundURL != "") { $backdropArray[] = $fullScreenBackgroundURL; }
				if ($previewFrameURL != "") { $backdropArray[] = $previewFrameURL; }
				
				
				
				
				
				
				$tomatoRating = $dC->tomatometerPercentage;
				
				$extras = array(
					"com.ceviixx.appleTV-API" => array(
						"rating" => array("com.ceviixx.appleTV-API" => $dT->averageRating),
						"poster" => $coverArray,
						"backdrop" => $backdropArray
					)
				);
				
				
				
				$release = date("Y-m-d", $dC->releaseDate / 1000);
				
				
				
				$synItems[] = array(
					"title" => "$dC->title",
					"tagline" => "",
					"original_available" => "$release",
					"original_title" => "ORIGINAL TITLE",
					"summary" => "$dC->description",
					"certificate" => "$rating",
					"genre" => $genres,
					"actor" => $actors,
					"director" => $directors,
					"writer" => $writers,
					"extra" => $extras
				);
				
				
				
				
				
				
				
				
				
			}
			
			
			
		}
		
		
		
	}
}


$resultArray = array(
	"success" => true,
	"result" => $synItems
);


$synoResult = json_encode($resultArray);















header('Content-Type: application/json');
echo json_encode(json_decode($synoResult), JSON_PRETTY_PRINT);

?>