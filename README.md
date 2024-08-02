# Data_Structure_in_Python

<h1 style="color: #0cb5f2;"><i>Sorting</i></h1>
<h2 style="color: orange;">Bubble Sort</h2>
<b>Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.</b>
<h4>Algorithm: </h4>
- traverse from left and compare adjacent elements and the higher one is placed at right side. <br>
- In this way, the largest element is moved to the rightmost end at first. <br>
- This process is then continued to find the second largest and place it and so on until the data is sorted.<br>
<hr>
<h2 style="color: orange;">Selection Sort</h2>
<b>The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.</b>
<h4>Algorithm : </h4>
- Go through the array to find the lowest value.<br>
- Move the lowest value to the front of the unsorted part of the array.<br>
- Go through the array again as many times as there are values in the array.<br>
<hr>
<h2 style="color: orange;">Insertion Sort</h2>
<b>The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.</b>
<h4>Algorithm : </h4>
- Take the first value from the unsorted part of the array.<br>
- Move the value into the correct place in the sorted part of the array.<br>
- Go through the unsorted part of the array again as many times as there are values.<br>
<hr>
<h2 style="color: orange;">Merge Sort</h2>
<b>The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, and then building the array back together the correct way so that it is sorted.</b>
<h4>Algorithm :</h4>
- Divide the unsorted array into two sub-arrays, half the size of the original.<br>
- Continue to divide the sub-arrays as long as the current piece of the array has more than one element.<br>
- Merge two sub-arrays together by always putting the lowest value first.<br>
- Keep merging until there are no sub-arrays left.<br>
<hr>


<br><br><br><br><br><br><br><br>
<hr>
<!-- Linked List Starts From Here -->
<h1 style="color: #0cb5f2;"><i>Linked Lists</i></h1>
<b>A Linked List is, as the word implies, a list where the nodes are linked together. Each node contains data and a pointer. The way they are linked together is that each node points to where in the memory the next node is placed.</b>

<h3 style="color: pink;">Types of Linked Lists : </h3>
<ul>
    <li><h4>Singly Linked Lists</h4></li>
    <li><h4>Doubly Linked Lists</h4></li>
    <li><h4>Circular Linked Lists</h4></li>
</ul>
<br>
<h3 style="color:grey;">Singly Linked List</h3>
A singly linked list consists of nodes where each node contains a data field and a reference (link) to the next node in the sequence.

<div>
<svg width="500" height="150">
  <!-- First Node -->
  <rect x="50" y="50" width="80" height="40" stroke="black" fill="none"/>
  <text x="75" y="75" font-family="Verdana" font-size="15" fill="black">Node 1</text>
  <line x1="130" y1="70" x2="180" y2="70" stroke="black" />

  <!-- Second Node -->
  <rect x="180" y="50" width="80" height="40" stroke="black" fill="none"/>
  <text x="205" y="75" font-family="Verdana" font-size="15" fill="black">Node 2</text>
  <line x1="260" y1="70" x2="310" y2="70" stroke="black" />

  <!-- Third Node -->
  <rect x="310" y="50" width="80" height="40" stroke="black" fill="none"/>
  <text x="335" y="75" font-family="Verdana" font-size="15" fill="black">Node 3</text>
  <line x1="390" y1="70" x2="440" y2="70" stroke="black" />
  <text x="450" y="75" font-family="Verdana" font-size="15" fill="black">NULL</text>
</svg>
</div>

