<p>#GP</p> 
</p>title : online detection of key events in football matches</p>
<p>summary</p>
<ul>
	<li> we removed crowd and detected playground using image processing techinques </li>
	<li> we detected the ball using its geometric features </li>
	<li> we detected the players using opencv's HOG classifier (terrible accuracy) </li>
	<li> we tracked the detected players using opencv's tracker and the "MIL" algorithm (great accuracy) </li>
	<li> we extracted key points using SURF and cluster the desciptors using SOM </li>
	<li> the vectors in the SOM form a kind of a visual language that allows us to make a bag of features for each image</li>
	<li> the used SOM had a 50x50 structre so we had 2500 "words" </li>
	<li> we collected a data set of 52000 images and labeled them </li>
	<li> we trained five backpropagation NN each to be abel to tell whether a certain event has occured or not untill each network had an accuracy of at least 80% </li>
	<li> we trained another network which takes the output of the previous 5 networks as input and outputs the correct label until its accuracy on testing data was 93% </li>
	<li> experimentation using PCA showed that we can achieve the same accuracy if we project each image representation (the 2500 vector from SOM) on a 140+ dimentional space </li>
</ul>
</li> guidlines for GP team </li>
<ul>
	<li> don't push unless the whole project works correctly on your machine </li>
	<li> don't add external library files in the project . </li>
	<li> if you use an extenal library modify this document and add its name/link to the dependecies section along with a link/tutorial on how to install and use it </li>
	<li> media resources(images/videos) should be added in the drive folder (link below) with BOTH  </li>
	<ul>
		<li> a note in the commit message </li>
		<li> and a comment in the code where it's used </li>
	</ul>
	<li> try to be as organised as possible </li>
	<li> write clear and clean code with comments </li>
	<li> if you choose to use an external library ,compare alternatives and choose the best in terms of quality and community support </li>
</ul>

note
<ul>
	<li> drive folder https://drive.google.com/drive/folders/0By6PnoxEQLnVZzdOMElIQlQ0bms?usp=sharing </li>
	<li> although lotfy said we should use python3 ,all the code he wrote so far is in python2.7 so we should stick to python2.7 </li>	
	<li> whenever we can we should use C++ or Java for peformence issues</li>
</ul>


dependencies/links:
<ul>
	<li> openCV  </li>
	<ul>
		<li> library link : https://github.com/opencv/opencv </li>
		<li> tutorials : http://docs.opencv.org/2.4/doc/tutorials/tutorials.html </li>		
	</ul>
	<li> BG-substraction Library : https://github.com/dparks1134/Background-Subtraction-Library </li>
	<li> joblib </li>
	<ul>
		<li> usage : to save models/objects to files and reading them back </li>
		<li> link : https://pythonhosted.org/joblib/ </li>
	</ul>
	<li> sklearn </li>
	<li> qt-4 </li>
</ul>
