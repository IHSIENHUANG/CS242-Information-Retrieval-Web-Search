<?php
  $item_count = 0;
  $rubbish_array = [];
  $tweet_id_array = [];
  $tweet_content_array = [];
  $followers_array = [];
  $location_array = [];
  $time_array = [];
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Creative - Bootstrap 3 Responsive Admin Template">
  <meta name="author" content="GeeksLabs">
  <meta name="keyword" content="Creative, Dashboard, Admin, Template, Theme, Bootstrap, Responsive, Retina, Minimal">
  <link rel="shortcut icon" href="img/icons/Twitter-icon.png">

  <title>Twitter Search Engine</title>

  <!-- Bootstrap CSS -->
  <link href="css/bootstrap.min.css" rel="stylesheet">
  <!-- bootstrap theme -->
  <link href="css/bootstrap-theme.css" rel="stylesheet">
  <!--external css-->
  <!-- font icon -->
  <link href="css/elegant-icons-style.css" rel="stylesheet" />
  <link href="css/font-awesome.min.css" rel="stylesheet" />
  <!-- full calendar css-->
  <link href="assets/fullcalendar/fullcalendar/bootstrap-fullcalendar.css" rel="stylesheet" />
  <link href="assets/fullcalendar/fullcalendar/fullcalendar.css" rel="stylesheet" />
  <!-- easy pie chart-->
  <link href="assets/jquery-easy-pie-chart/jquery.easy-pie-chart.css" rel="stylesheet" type="text/css" media="screen" />
  <!-- owl carousel -->
  <link rel="stylesheet" href="css/owl.carousel.css" type="text/css">
  <link href="css/jquery-jvectormap-1.2.2.css" rel="stylesheet">
  <!-- Custom styles -->
  <link rel="stylesheet" href="css/fullcalendar.css">
  <link href="css/widgets.css" rel="stylesheet">
  <link href="css/style.css" rel="stylesheet">
  <link href="css/style-responsive.css" rel="stylesheet" />
  <link href="css/xcharts.min.css" rel=" stylesheet">
  <link href="css/jquery-ui-1.10.4.min.css" rel="stylesheet">
  <!-- =======================================================
    Theme Name: NiceAdmin
    Theme URL: https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/
    Author: BootstrapMade
    Author URL: https://bootstrapmade.com
  ======================================================= -->
  <style>
    .lite{
      color: #ffffff !important;
      font-weight: bold;  
    }
    .navbar-form .form-control {
      position: relative;
      font-size: 16px;
      height: 30px;
      width: 500px;
      padding: 10px;
      background: white;
      -webkit-box-sizing: border-box;
      -moz-box-sizing: border-box;
      box-sizing: border-box;
    }
  </style>
</head>

<body>
  <!-- container section start -->
  <section id="container" class="">


    <header class="header dark-bg">
      <div class="toggle-nav">
        <div class="icon-reorder tooltips" data-placement="bottom"><i class="icon_menu"></i></div>
      </div>

      <!--logo start-->
      <a class="logo"><span class="lite">Lucene Search Engine</span></a>
      <!--logo end-->

      <div class="nav search-row" id="top_menu">
        <!--  search form start -->
        <ul class="nav top-menu">
          <li>
            <form class="navbar-form" method="post" enctype="multipart/form-data">
              <input class="form-control" placeholder="Search" type="text" name="ta1">
              <input type="submit" class="btn btn-primary" value="Submit Query" />
            </form>
          </li>
        </ul>
        <!--  search form end -->
      </div>
    </header>
    <!--header end-->

    <!--sidebar start-->
    <aside>
      <div id="sidebar" class="nav-collapse ">
        <!-- sidebar menu start-->
        <ul class="sidebar-menu">
          <li class="active">
            <a class="" href="index2-bm.php">
                          <i class="icon_table"></i>
                          <span>Hadoop</span>
                      </a>
          </li>

          <li class="active">
            <a class="" href="index2-lucene.php">
                          <i class="icon_documents_alt"></i>
                          <span>Lucene</span>
                      </a>
          </li>
        </ul>
        <!-- sidebar menu end-->
      </div>
    </aside>
    <!--sidebar end-->

    <!--main content start-->
    <section id="main-content">
      <section class="wrapper">
        <!--overview start-->
        <div class="row">
          <div class="col-lg-12">
            <h3 class="page-header"><i class="fa fa-laptop"></i> Search Results - Lucene (Popularity)</h3>
            <ol class="breadcrumb">
              <li><i class="fa fa-home"></i><a href="../index.html">Home</a></li>
              <li><i class="fa fa-laptop"></i>Search Results - Hadoop (Popularity)</li>
            </ol>
          </div>
        </div>

        <div class="row">
          
          <a href="index2-lucene.php" class="fill-div">
            <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12">
              <div class="info-box dark-bg">
                <i class="fa fa-thumbs-o-up"></i>
                <div class="count">Popularity</div>
                <div class="title">Rerank</div>
              </div> <!--/.info-box-->
            </div> <!--/.col-->
          </a>

        </div>
        <!--/.row-->

        <p><?php 
          if ($_SERVER['REQUEST_METHOD'] == 'POST') { 
            error_reporting(E_ALL);

            $ta1 = $_POST['ta1'];
	    exec("python stem_query.py '$ta1'", $ta2);
            $existing  = "existing text";
            exec("java -jar lucene.jar '$ta2[0]'", $output);
            // DEBUG: fetched array
            foreach($output as $item) {
              $item_count ++;
            //   echo $item;
            //   echo "<br>";
            }
            // echo $item_count;
            $b = 0;
            for($a=0; $a<$item_count-1; $a+=5) {
              $tweet_id_array[$b] = $output[$a];
              $tweet_content_array[$b] = $output[$a+1];
              $followers_array[$b] = $output[$a+2];
              $location_array[$b] = $output[$a+3];
              $time_array[$b] = $output[$a+4];
              $b++;
            }
          }
        ?></p>


        <div class="row">
          <?php
            for($a=0; $a<$item_count/5-1; $a++) {
            echo '<div class="col-lg-9 col-md-12">';
              echo '<div class="panel panel-default">';
                echo '<div class="panel-heading">';
                  echo '<h2><i class="fa fa-flag-o red"></i><strong>Tweet Result # '.($a+1).'</strong></h2>';
                  echo '<div class="panel-actions">';
                    echo '<a href="index.html#" class="btn-setting"><i class="fa fa-rotate-right"></i></a>';
                    echo '<a href="index.html#" class="btn-minimize"><i class="fa fa-chevron-up"></i></a>';
                    echo '<a href="index.html#" class="btn-close"><i class="fa fa-times"></i></a>';
                  echo '</div>';
                echo '</div>';
                echo '<div class="panel-body">';
                  echo '<table class="table bootstrap-datatable countries">';
                    echo '<thead>';
                      echo '<tr>';
                        echo '<th></th>';
                        echo '<th>Twitter Name</th>';
                        echo '<th>Tweet Content</th>';
                        echo '<th>Followers</th>';
                        echo '<th>Location</th>';
                        echo '<th>Time</th>';
                      echo '</tr>';
                    echo '</thead>';
                    echo '<tbody>';

                        echo "<tr>";
                          echo '<td><img src="img/icons/Twitter-icon.png" style="height:18px; margin-top:-2px;"></td>';
			  $str1 = preg_replace("/($ta2[0])/i","<b style='color:red'>$1</b>",$tweet_id_array[$a]);
			  $str2 = preg_replace("/($ta2[0])/i","<b style='color:red'>$1</b>",$tweet_content_array[$a]);
			  $str3 = preg_replace("/($ta2[0])/i","<b style='color:red'>$1</b>",$followers_array[$a]);
			  $str4 = preg_replace("/($ta2[0])/i","<b style='color:red'>$1</b>",$location_array[$a]);
			  $str5 = preg_replace("/($ta2[0])/i","<b style='color:red'>$1</b>",$time_array[$a]);
                          echo '<td>'.$str1.'</td>';
                          echo '<td>'.$str2.'</td>';
                          echo '<td>'.$str3.'</td>';
                          echo '<td>'.$str4.'</td>';
                          echo '<td>'.$str5.'</td>';
                        echo "</tr>";
                      
                    echo '</tbody>';
                  echo '</table>';
                echo '</div>';

              echo '</div>';

            echo '</div>';
          }
        ?>

        </div>
        <!-- statics end -->




        

      </section>
      <div class="text-right">
        <div class="credits">
          <!--
            All the links in the footer should remain intact.
            You can delete the links only if you purchased the pro version.
            Licensing information: https://bootstrapmade.com/license/
            Purchase the pro version form: https://bootstrapmade.com/buy/?theme=NiceAdmin
          -->
        </div>
      </div>
    </section>
    <!--main content end-->
  </section>
  <!-- container section start -->

  <!-- javascripts -->
  <script src="js/jquery.js"></script>
  <script src="js/jquery-ui-1.10.4.min.js"></script>
  <script src="js/jquery-1.8.3.min.js"></script>
  <script type="text/javascript" src="js/jquery-ui-1.9.2.custom.min.js"></script>
  <!-- bootstrap -->
  <script src="js/bootstrap.min.js"></script>
  <!-- nice scroll -->
  <script src="js/jquery.scrollTo.min.js"></script>
  <script src="js/jquery.nicescroll.js" type="text/javascript"></script>
  <!-- charts scripts -->
  <script src="assets/jquery-knob/js/jquery.knob.js"></script>
  <script src="js/jquery.sparkline.js" type="text/javascript"></script>
  <script src="assets/jquery-easy-pie-chart/jquery.easy-pie-chart.js"></script>
  <script src="js/owl.carousel.js"></script>
  <!-- jQuery full calendar -->
  <<script src="js/fullcalendar.min.js"></script>
    <!-- Full Google Calendar - Calendar -->
    <script src="assets/fullcalendar/fullcalendar/fullcalendar.js"></script>
    <!--script for this page only-->
    <script src="js/calendar-custom.js"></script>
    <script src="js/jquery.rateit.min.js"></script>
    <!-- custom select -->
    <script src="js/jquery.customSelect.min.js"></script>
    <script src="assets/chart-master/Chart.js"></script>

    <!--custome script for all page-->
    <script src="js/scripts.js"></script>
    <!-- custom script for this page-->
    <script src="js/sparkline-chart.js"></script>
    <script src="js/easy-pie-chart.js"></script>
    <script src="js/jquery-jvectormap-1.2.2.min.js"></script>
    <script src="js/jquery-jvectormap-world-mill-en.js"></script>
    <script src="js/xcharts.min.js"></script>
    <script src="js/jquery.autosize.min.js"></script>
    <script src="js/jquery.placeholder.min.js"></script>
    <script src="js/gdp-data.js"></script>
    <script src="js/morris.min.js"></script>
    <script src="js/sparklines.js"></script>
    <script src="js/charts.js"></script>
    <script src="js/jquery.slimscroll.min.js"></script>
    <script>
      //knob
      $(function() {
        $(".knob").knob({
          'draw': function() {
            $(this.i).val(this.cv + '%')
          }
        })
      });

      //carousel
      $(document).ready(function() {
        $("#owl-slider").owlCarousel({
          navigation: true,
          slideSpeed: 300,
          paginationSpeed: 400,
          singleItem: true

        });
      });

      //custom select box

      $(function() {
        $('select.styled').customSelect();
      });

      /* ---------- Map ---------- */
      $(function() {
        $('#map').vectorMap({
          map: 'world_mill_en',
          series: {
            regions: [{
              values: gdpData,
              scale: ['#000', '#000'],
              normalizeFunction: 'polynomial'
            }]
          },
          backgroundColor: '#eef3f7',
          onLabelShow: function(e, el, code) {
            el.html(el.html() + ' (GDP - ' + gdpData[code] + ')');
          }
        });
      });
    </script>

</body>

</html>
