# CSS3 Interview Questions and Answers

### Q: Explain CSS Box Model.

#### Answer

-   A: The CSS box model is essentially a box that wraps around every
    HTML element. It consists of: margins, borders, padding, and the
    actual content. The image below illustrates the box model.

-   _Important:_ When you set the width and height properties of
    an element with CSS, you just set the width and height of the content
    area. To calculate the full size of an element, you must also add
    padding, borders and margins.

-   _Note for old IE:_ Internet Explorer 8 and earlier versions,
    include padding and border in the width property. To fix this problem,
    add a &lt;!DOCTYPE html> to the HTML page.
    ![Box Model](img/CSS_Box_Model.png)

* * *

### Q: What is universal selector?

-   Rather than selecting elements of a specific type, the universal selector quite simply matches the name of any element type &lt;body>

```css
* {
  color: #000000;
  }
```

-   This rule renders the content of every element in our document in black.

* * *

### Q: How CSS style overriding works?

-   Following is the rule to override any Style Sheet Rule −

    -   Any inline style sheet takes highest priority. So, it will override any rule defined in &lt;style>...&lt;/style> tags or rules defined in any external style sheet file.

    -   Any rule defined in &lt;style>...&lt;/style> tags will override rules defined in any external style sheet file.

    -   Any rule defined in external style sheet file takes lowest priority, and rules defined in this file will be applied only when above two rules are not applicable.

* * *

### In CSS3, how would you select:

-   Every <a> element whose href attribute value begins with “https”.
-   Every <a> element whose href attribute value ends with “.pdf”.
-   Every <a> element whose href attribute value contains the substring “css”.

#### Answer

Select every &lt;a> element whose href attribute value begins with “https”:

```css
    a[href^="https"]
```

Select every &lt;a> element whose href attribute value ends with “.pdf”:

```css
    a[href$=".pdf"]
```

Select every &lt;a> element whose href attribute value contains the substring “css”:

```css
    a[href*="css"]
```

* * *

### Given the following HTML:

```html
<div id="page">
  <h1>Heading Title</h1>
  <h2>Subheading Title</h2>
  <h2>Subheading Title</h2>
  <h1>Heading Title</h1>
  <h2>Subheading Title</h2>
  <h1>Heading Title</h1>
</div>
```

How could you use CSS to achieve the following automatic numbering:

    1.  Heading Title
    1.1) Subheading title
    1.2) Subheading Title
    1.  Heading Title
    2.1) Subheading Title
    1.  Heading Title

#### Answer

The following CSS will achieve this type of automatic numbering:

```css
#page {
  counter-reset: heading;
}
h1:before {
  content: counter(heading)") ";
  counter-increment: heading;
}
h1 {
  counter-reset: subheading;
}
h2:before {
  content: counter(heading)"." counter(subheading)") ";
  counter-increment: subheading;
}
```

* * *

### What are pseudo classes and what are they used for?

#### Answer

Pseudo classes are similar to classes, but are not explicitly defined in
the markup, and are used to add additional effects to selected HTML
elements such as link colors, hover actions, etc. Pseudo classes are
defined by first listing the selector, followed by a colon and then
pseudo-class element. E.g., a:link{ color: blue }, or a:visited { color:
red } Pseudo-class syntax: selector:pseudo-class { property:value;}

Syntax for using a pseudo class within a CSS class:
selector.class:pseudo-class { property:value;}

_:link, :visited, :hover, :active, :first~line~_ are all examples of
pseudo classes, used to call a specific action on an element, such as
the changing of a link color after it has been visited.

* * *

### All CSS Pseudo Classes

| Selector             | Example               | Example description                                                                                      |
| -------------------- | --------------------- | -------------------------------------------------------------------------------------------------------- |
| :active              | a:active              | Selects the active link                                                                                  |
| :checked             | input:checked         | Selects every checked `<input>` element                                                                  |
| :disabled            | input:disabled        | Selects every disabled `<input>` element                                                                 |
| :empty               | p:empty               | Selects every `<p>` element that has no children                                                         |
| :enabled             | input:enabled         | Selects every enabled `<input>` element                                                                  |
| :first-child         | p:first-child         | Selects every `<p>` elements that is the first child of its parent                                       |
| :first-of-type       | p:first-of-type       | Selects every `<p>` element that is the first `<p>` element of its parent                                |
| :focus               | input:focus           | Selects the `<input>` element that has focus                                                             |
| :hover               | a:hover               | Selects links on mouse over                                                                              |
| :in-range            | input:in-range        | Selects `<input>` elements with a value within a specified range                                         |
| :invalid             | input:invalid         | Selects all `<input>` elements with an invalid value                                                     |
| :lang(_language_)    | p:lang(it)            | Selects every `<p>` element with a lang attribute value starting with "it"                               |
| :last-child          | p:last-child          | Selects every `<p>` elements that is the last child of its parent                                        |
| :last-of-type        | p:last-of-type        | Selects every `<p>` element that is the last `<p>` element of its parent                                 |
| :link                | a:link                | Selects all unvisited links                                                                              |
| :not(selector)       | :not(p)               | Selects every element that is not a `<p>` element                                                        |
| :nth-child(n)        | p:nth-child(2)        | Selects every `<p>` element that is the second child of its parent                                       |
| :nth-last-child(n)   | p:nth-last-child(2)   | Selects every `<p>` element that is the second child of its parent, counting from the last child         |
| :nth-last-of-type(n) | p:nth-last-of-type(2) | Selects every `<p>` element that is the second `<p>` element of its parent, counting from the last child |
| :nth-of-type(n)      | p:nth-of-type(2)      | Selects every `<p>` element that is the second `<p>` element of its parent                               |
| :only-of-type        | p:only-of-type        | Selects every `<p>` element that is the only `<p>` element of its parent                                 |
| :only-child          | p:only-child          | Selects every `<p>` element that is the only child of its parent                                         |
| :optional            | input:optional        | Selects `<input>` elements with no "required" attribute                                                  |
| :out-of-range        | input:out-of-range    | Selects `<input>` elements with a value outside a specified range                                        |
| :read-only           | input:read-only       | Selects `<input>` elements with a "readonly" attribute specified                                         |
| :read-write          | input:read-write      | Selects `<input>` elements with no "readonly" attribute                                                  |
| :required            | input:required        | Selects `<input>` elements with a "required" attribute specified                                         |
| :root                | root                  | Selects the document's root element                                                                      |
| :target              | #news:target          | Selects the current active #news element (clicked on a URL containing that anchor name)                  |
| :valid               | input:valid           | Selects all `<input>` elements with a valid value                                                        |
| :visited             | a:visited             | Selects all visited links                                                                                |

* * *

### All CSS Pseudo Elements

| Selector       | Example         | Example description                                          |
| -------------- | --------------- | ------------------------------------------------------------ |
| ::after        | p::after        | Insert content after every <p> element                       |
| ::before       | p::before       | Insert content before every <p> element                      |
| ::first-letter | p::first-letter | Selects the first letter of every <p> element                |
| ::first-line   | p::first-line   | Selects the first line of every <p> element                  |
| ::selection    | p::selection    | Selects the portion of an element that is selected by a user |

* * *

### How is the float property implemented in CSS?

#### Answer

-   Floats allow an element to be positioned horizontally, allowing elements below the floated element to flow around it.
-   Several floating elements can be placed together to make a gallery type layout.
-   Floats can only accept a left or right value.

```css
img {
float: right;
width: 50px;
margin: 5px;
}
```

To prevent subsequent elements from flowing around the floated element, pass in the clear property, followed by the side you wish to disable (i.e., ‘left’, ‘right’, ‘both’).

* * *

### How are inline and block elements different from each other?

#### Answer

-   A block element is an element that takes up the full width available, and has a line break before and after it. `<h1>, <p>, <li>, and <div>` are all examples of block elements.
-   An inline element only takes up as much width as necessary, cannot accept width and height values, and does not force line breaks. <a> and <span> are examples of inline elements.

* * *

### What is the purpose of the z-index and how is it used?

#### Answer

-   The z-index helps specify the stack order of positioned elements that may overlap one another.
-   The z-index default value is zero, and can take on either a positive or negative number.
-   An element with a higher z-index is always stacked above one with a lower index.
-   Z-Index can take the following values:
    -   Auto: Sets the stack order equal to its parents.
    -   Number: Orders the stack order.
    -   Initial: Sets this property to its default value (0).
    -   Inherit: Inherits this property from its parent element.

* * *

### What are the various techniques for clearing floats?

#### Answer

-   At some point or another, you will likely experience a collapsed float, which you will need to address.
-   This can be accomplished several ways, including using a clearfix2, by floating the parent element of the collapsed element, or by using an overflow property3.

* * *

### Explain the difference between visibility:hidden and display:none

#### Answer

-   visibility:hidden simply hides the element, while it will still take up space and affect the layout of the document.
-   display:none also hides the element, but will not take up space and the page will appear as if the element is not present.

* * *

### What are some of the new features and properties in CSS3?

#### Answer

-   Box model
-   New Web fonts
-   Rounded corners
-   Border Images
-   Box Shadows, Text Shadows
-   New Color schemes (RGBA)
-   Transform property
-   New Pseudo-classes
-   Multi-column layout
-   New Gradients

* * *

### Why shouldn’t I use fixed sized fonts ?

#### Answer

-   Often times, fixed font sizes will show up incorrectly on the user end and will prohibit responsiveness.
-   Using relative sizing will keep fonts proportionate in their relationships to each other and will allow for greater end user flexibility.

* * *

### Center item vertically

```html
<div class="center">
  <p>I am vertically and horizontally centered.</p>
</div>
```

#### Answer

```css
.center {
    height: 200px;
    position: relative;
    border: 3px solid green;
}

.center p {
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```

* * *

### What is CSS combinator?

#### Answer

-   A combinator is something that explains the relationship between the selectors.
-   A CSS selector can contain more than one simple selector. Between the simple selectors, we can include a combinator.
-   There are four different combinators in CSS3:

    -   _descendant selector (space)_: The descendant selector matches all elements that are descendants of a specified element.
    -   _child selector (>)_: The child selector selects all elements that are the immediate children of a specified element.
    -   _adjacent sibling selector (+)_: The adjacent sibling selector selects all elements that are the adjacent siblings of a specified element.
        Sibling elements must have the same parent element, and "adjacent" means "immediately following".
    -   _general sibling selector (~)_: The general sibling selector selects all elements that are siblings of a specified element.

* * *

### implement full-height fixed vertical navbar

#### Answer

```html
<ul>
  <li><a class="active" href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li><a href="#about">About</a></li>
</ul>
```

```css
body {
    margin: 0;
}

ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    width: 25%;
    background-color: #f1f1f1;
    position: fixed;
    height: 100%;
    overflow: auto;
}

li a {
    display: block;
    color: #000;
    padding: 8px 16px;
    text-decoration: none;
}

li a.active {
    background-color: #4CAF50;
    color: white;
}

li a:hover:not(.active) {
    background-color: #555;
    color: white;
}
```

* * *

### Implement horizontal navigation bar

#### Answer

```html
<ul>
  <li><a class="active" href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li><a href="#about">About</a></li>
</ul>
```

```css
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}

li {
    float: left;
}

li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

li a:hover {
    background-color: #111;
}
```

* * *

### Implement dropdown list

#### Answer

```html
<div class="dropdown">
  <button class="dropbtn">Dropdown</button>
  <div class="dropdown-content">
    <a href="#">Link 1</a>
    <a href="#">Link 2</a>
    <a href="#">Link 3</a>
  </div>
</div>
```

```css
/* Style The Dropdown Button */
.dropbtn {
    background-color: #4CAF50;
    color: white;
    padding: 16px;
    font-size: 16px;
    border: none;
    cursor: pointer;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
    position: relative;
    display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #f1f1f1}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
    display: block;
}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {
    background-color: #3e8e41;
}
```

* * *

### implement tooltip using css

#### Answer

```html
<div class="tooltip">Hover over me
  <span class="tooltiptext">Tooltip text</span>
</div>
```

```css
.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: black;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;
    position: absolute;
    z-index: 1;
    bottom: 100%;
    left: 50%;
    margin-left: -60px;

    /* Fade in tooltip - takes 1 second to go from 0% to 100% opac: */
    opacity: 0;
    transition: opacity 1s;
}

.tooltip:hover .tooltiptext {
    visibility: visible;
    opacity: 1;
}
```

* * *

### using image sprites - create a navigation list

#### Answer

```html
<ul id="navlist">
  <li id="home"><a href="default.asp"></a></li>
  <li id="prev"><a href="css_intro.asp"></a></li>
  <li id="next"><a href="css_syntax.asp"></a></li>
</ul>
```

```css
#navlist {
    position: relative;
}

#navlist li {
    margin: 0;
    padding: 0;
    list-style: none;
    position: absolute;
    top: 0;
}

#navlist li, #navlist a {
    height: 44px;
    display: block;
}

#home {
    left: 0px;
    width: 46px;
    background: url('img_navsprites.gif') 0 0; /* (left 0px, top 0px)
}

#prev {
    left: 63px;
    width: 43px;
    background: url('img_navsprites.gif') -47px 0;
}

#next {
    left: 129px;
    width: 43px;
    background: url('img_navsprites.gif') -91px 0;
}
```

### Implement image slide overlay

#### Answer

```html
<div class="container">
  <img src="img_avatar.png" alt="Avatar" class="image">
  <div class="overlay">
    <div class="text">Hello World</div>
  </div>
</div>
```

```css
.container {
  position: relative;
  width: 50%;
}

.image {
  display: block;
  width: 100%;
  height: auto;
}

.overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #008CBA;
  overflow: hidden;
  width: 100%;
  height: 0;
  transition: .5s ease;
}

.container:hover .overlay {
  height: 100%;
}

.text {
  white-space: nowrap;
  color: white;
  font-size: 20px;
  position: absolute;
  overflow: hidden;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
}
```

* * *

### what is CSS3 box-sizing property

#### Answer

The CSS3 box-sizing property allows us to include the padding and border in an element's total width and height.

If you set `box-sizing: border-box;` on an element padding and border are included in the width and height

* * *

### what is CSS3 Flexbox

#### Answer

Flexible boxes, or flexbox, is a new layout mode in CSS3.

Use of flexbox ensures that elements behave predictably when the page layout must accommodate different screen sizes and different display devices.

* * *

### What is the difference between flexbox model and the block model

#### Answer

For many applications, the flexible box model provides an improvement over the block model in that it does not use floats,
nor do the flex container's margins collapse with the margins of its contents

* * *

### Note

#### Note: Flexbox layout is most appropriate to the components of an application, and small-scale layouts, while the Grid layout is intended for larger scale layouts.
