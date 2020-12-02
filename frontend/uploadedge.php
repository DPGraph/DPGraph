<!DOCTYPE html>
<html>
  <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
    <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="css/modern-business.css" rel="stylesheet">

  <!-- Vega -->
  <script src="https://vega.github.io/vega/vega.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@3"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@5"></script>

  <!-- Plotly-->
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

  </head>
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark fixed-top">
    <div class="container">
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="index.html">DPGraph</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="problem.html">Problem Statement</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="frontier.html">Accuracy Frontier</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="finding.html">Empirical Findings</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownBlog" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Background Overview
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownBlog">
              <a class="dropdown-item" href="glossary.html">Reference: Glossary</a>
              <a class="dropdown-item" href="dataset.html">Reference: Dataset</a>
              <a class="dropdown-item" href="algorithm.html">Reference: Algorithms</a>
              <a class="dropdown-item" href="DPdefinition.html">Reference: Differential Privacy</a>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <br>
  

<div class="container">
        <body >
        <select id = "Degree Type" onchange = "frontierFn()"> 
        <option value = "2" selected = "selected">Edge DP</option>
        
        </select>

        <select id = "Utility"> 
        <option value = "1" selected = "selected">Degree Distribution</option>
        <option value = "2">Subgraph Counting_4kclique</option>
        <option value = "3">Subgraph Counting_3kstar</option>
        <option value = "4">Subgraph Counting_2ktriangle</option>
        <option value = "5">Subgraph Counting_triangle</option>
        </select>
  <select id = "Dataset"> 
  <option value = "1">FACEBOOK</option>
  </select>  
  <p> Here is the result by compiling the python file you have uploaded:</p> 
  
    <script type="text/javascript">
      function hideoption(){
        document.getElementById("show_algorithm").style.visibility = "hidden";
        document.getElementById("select_algorithm_DD").style.visibility = "hidden";
        document.getElementById("algorithm1").checked = true;
        document.getElementById("algorithm1").style.visibility = "hidden";
        document.getElementById("algorithm2").style.visibility = "hidden";
        document.getElementById("algorithm3").style.visibility = "hidden";
        document.getElementById("algorithm4").style.visibility = "hidden";
        document.getElementById("algorithm5").style.visibility = "hidden";
        document.getElementById("algorithm6").style.visibility = "hidden";
        document.getElementById("algorithm2").checked = true;
        document.getElementById("algorithm3").checked = true;
        document.getElementById("algorithm4").checked = true;
        document.getElementById("algorithm5").checked = true;
        document.getElementById("algorithm6").checked = true;
      }
 
  function prepare(){
    hideoption();
    document.getElementById("true_explain").style.visibility = "hidden";
    document.getElementById("noisy_explain").style.visibility = "hidden";
    document.getElementById("noisy_detail").style.visibility = "hidden";
    document.getElementById("Dataset").style.visibility = "hidden";
    document.getElementById("Utility").style.visibility = "hidden";
    document.getElementById("Degree Type").style.visibility = "hidden";
    
  }
          var data = {};
          var curveChosen = '';
          var eChosen = '';
          var rankChosen = '';
          var time = 6;
          var algoindex = {};
          var algorithms = {};
          var edgealgoindex = {};
          var edgealgorithms = {};
          function getxrange(){
            var temp_data = document.getElementById("Dataset").value;
            if(temp_data == 1) return [0,300]
            else if(temp_data == 2) return [0,200]
            else if(temp_data == 3) return [0,100]
            else if(temp_data == 4) return [0,300]
            else if(temp_data == 5) return [0,10]
            else if(temp_data == 6) return [0,300]
          }
          function getyrange(){
            var temp_data = document.getElementById("Dataset").value;
            if(temp_data == 1) return [0,120]
            else if(temp_data == 2) return [0,1500]
            else if(temp_data == 3) return [0,10000]
            else if(temp_data == 4) return [0,300]
            else if(temp_data == 5) return [0,5]
            else if(temp_data == 6) return [0,500]
          }
          function show_algorithm(){
            buttonTextFn();
            var dp_chosen = document.getElementById("Degree Type").value;
            if(document.getElementById("select_algorithm_DD").style.visibility != "visible"){
              document.getElementById("select_algorithm_DD").style.visibility = "visible";
              document.getElementById("algorithm3").style.visibility = "visible";
              document.getElementById("algorithm4").style.visibility = "visible";
              document.getElementById("algorithm5").style.visibility = "visible";
              document.getElementById("algorithm6").style.visibility = "visible";
              document.getElementById("algorithm1").style.visibility = "visible";
              document.getElementById("algorithm2").style.visibility = "visible";
              //document.getElementById("algorithm7").style.visibility = "visible";
              if(dp_chosen == 1) {
                document.getElementById("nodedp_algo1").style.display = "inline";
                document.getElementById("edgedp_algo1").style.display = "none";
                document.getElementById("nodedp_algo2").style.display = "inline";
                document.getElementById("edgedp_algo2").style.display = "none";
                document.getElementById("algorithm3").style.visibility = "visible";
                document.getElementById("nodedp_algo3").style.display = "inline";
                document.getElementById("algorithm4").style.visibility = "visible";
                document.getElementById("nodedp_algo4").style.display = "inline";
                document.getElementById("algorithm5").style.visibility = "visible";
                document.getElementById("nodedp_algo5").style.display = "inline";
                document.getElementById("algorithm6").style.visibility = "visible";
                document.getElementById("nodedp_algo6").style.display = "inline";
                //document.getElementById("algorithm7").style.visibility = "visible";
                //document.getElementById("nodedp_algo7").style.display = "inline";
              } 
              else {
                document.getElementById("nodedp_algo1").style.display = "none";
                document.getElementById("edgedp_algo1").style.display = "inline";
                document.getElementById("nodedp_algo2").style.display = "none";
                document.getElementById("edgedp_algo2").style.display = "inline";
                document.getElementById("nodedp_algo3").style.display = "none";
                document.getElementById("edgedp_algo3").style.display = "inline";
                document.getElementById("algorithm3").style.visibility = "visible";
                document.getElementById("algorithm4").style.visibility = "hidden";
                document.getElementById("nodedp_algo4").style.display = "none";
                document.getElementById("algorithm5").style.visibility = "hidden";
                document.getElementById("nodedp_algo5").style.display = "none";
                document.getElementById("algorithm6").style.visibility = "hidden";
                document.getElementById("nodedp_algo6").style.display = "none";
                //document.getElementById("algorithm7").style.visibility = "hidden";
                //document.getElementById("nodedp_algo7").style.display = "none";
              }
            } else {
              document.getElementById("select_algorithm_DD").style.visibility = "hidden";
              document.getElementById("algorithm3").style.visibility = "hidden";
              document.getElementById("algorithm4").style.visibility = "hidden";
              document.getElementById("algorithm5").style.visibility = "hidden";
              document.getElementById("algorithm6").style.visibility = "hidden";
              document.getElementById("algorithm1").style.visibility = "hidden";
              document.getElementById("algorithm2").style.visibility = "hidden";
              //document.getElementById("algorithm7").style.visibility = "hidden";
            }
          }
          function plotfrontier(dataChosen){
            var dp_chosen = document.getElementById("Degree Type").value;
            if(dp_chosen == 2) var csvName = 'uploads/'+dataChosen + 'edge.csv';
            else var csvName = 'uploads/'+dataChosen + '.csv';
            
            Plotly.d3.csv(csvName, (err, rows) => {
              var tempPlot = document.getElementById('scatterFrontier')
              function getcolor(y){
                if (y == 1) return '#c83349';
                else if(y == 2) return '#622569';
                else return '94b1d2';
              }
              if(dp_chosen == 1){
                function getwidth(y){
                  if(y==3)return 3;
                  else return 1;
                }
                var data = algoindex.map(y => {
                  var d = rows.filter(r => r.algorithm == y)    
                  return {
                    name: algorithms[y-1],
                    x: d.map(r => r.epsilon),
                    y: d.map(r => r.L1error),
                    marker:{
                      color:getcolor(y)
                    },
                    width: getwidth(y),
                    error_y: {
                      type: 'data',
                      array: d.map(r => r.L1error_sd),
                      visible: true
                    },
                    type: 'scatter'
                  }
                })
              } else {
                function getwidthedge(y){
                  if(y==3)return 3;
                  else return 1;
                }
                var data = edgealgoindex.map(y => {
                  var d = rows.filter(r => r.algorithm == y)    
                  return {
                    name: algorithms[y-1],
                    x: d.map(r => r.epsilon),
                    y: d.map(r => r.L1error),
                    marker:{
                      color: getcolor(y)
                    },
                    width: getwidthedge(y),
                    error_y: {
                      type: 'data',
                      array: d.map(r => r.L1error_sd),
                      visible: true,
                    },
                    type: 'scatter'
                  }
                })
                
              }
              var temp_query = document.getElementById("Utility").value;
              function gettitle(){
                if(temp_query == 1) return 'L1error';
                else return 'Relative error';
              }
              var layout = {
                autosize: false,
                width: 300,
                height: 300,
                xaxis: {
                  automargin: true,
                  type: 'log',
                  title: {
                    text: 'epsilon',
                    standoff: 1,
                  },
                  autorange: true,
                  tickangle: 'auto',
                  tickfont: {
                    family: 'Old Standard TT, serif',
                    size: 14,
                    color: 'lightgrey'
                  },
                  titlefont: {
                    family: 'Arial, sans-serif',
                    size: 18,
                    color: 'black'
                  },
                },
                yaxis:{
                  automargin: true,
                  title: {
                    text: gettitle(),
                    standoff: 1,
                  },
                  autorange: false,
                  range: [0,3],
                  tickangle: 45,
                  titlefont: {
                    family: 'Arial, sans-serif',
                    size: 18,
                    color: 'black'
                  },
                  tickfont: {
                    family: 'Old Standard TT, serif',
                    size: 14,
                    color: 'lightgrey'
                  },
                  exponentformat: 'e',
                  showexponent: 'all',
                  hoverformat: '.2r',
                },
                margin: {
                  l: 30,
                  r: 30,
                  b: 30,
                  t: 35,
                  pad: 4
                },
                mode:'markers',
                hovermode:'closest',
                title:'Accuracy Frontier FACEBOOK',
                showlegend: false
              };
                
              Plotly.newPlot('scatterFrontier', data, layout,{showSendToCloud: true});
              document.getElementById("true_explain").style.visibility = "visible";
              var time = 0;
                // This function below determines which noisy histogram to display, based on the point that user clicked on the frontier.
              tempPlot.on('plotly_click', function(data){
                // To uniquely identify which noisy histogram we want to display, we need 1) algorithm 2) epsilon value (x-value)
                var curr_time = new Date();
                var pts = '';
                Plotly.deleteTraces('noisyHist', 1);
                Plotly.deleteTraces('trueHist', 1);
                for(var i=0; i < data.points.length; i++){
                  rankChosen = data.points[i].curveNumber;
                    if (dp_chosen == 1){
                      if (rankChosen == 0) {
                        curveChosen = "nodeDP_degHis_Lap";
                      } else if (rankChosen == 1) {
                        curveChosen = "nodeDP_degSeq_Lap";
                      } else if (rankChosen == 2){
                        curveChosen = "nodeDP_nodeTrun_Smooth";
                      } else if (rankChosen == 3){
                        curveChosen = "nodeDP_edgeAdd_degHisPart_Lap";
                      } else if (rankChosen == 4){
                        curveChosen = "nodeDP_edgeAdd_degCum_Lap";
                      } else if (rankChosen == 5){
                        curveChosen = "nodeDP_edgeAdd_degCum_Lap_variant";
                      } 
                    } else {
                      if(rankChosen == 0){
                        curveChosen = "edgeDP_degHis_lap";
                      } else if(rankChosen == 1){
                        curveChosen = "edgeDP_degHis_lap";
                      }
                    }
                    eChosen = data.points[i].x.toPrecision(1);                  
                      // Based on the dataset, algorithm, and epsilon level chosen, we determine the name of the CSV file
                      // that store the noisy histogram user has chosen 
                    var testHeight = 300; // this simply tests that we can use variables for layout parameters
                      // The following function plost the noisy histogram
                    if(dp_chosen==1) var noisyHistName ='uploads/'+dataChosen+"algo.csv"
                    else var noisyHistName = 'uploads/'+dataChosen + "edgealgo.csv"
                    console.log("Epsilon Chosen is "+eChosen);
                    //noisyHistName = "outputmodify.csv"
                    if(eChosen == 1) eChosen = 1.0
                    else if(eChosen == 2) eChosen = 2.0
                    else if(eChosen == 5) eChosen = 5.0
                    else if(eChosen == 10) eChosen = 10.0
                    Plotly.d3.csv(noisyHistName, function(err, rows){
                      var d = rows.filter(r => ((r.epsilon == eChosen) && (r.algorithm == rankChosen+1)));
                      if(dp_chosen == 1) var aname = algorithms[rankChosen];
                      else var aname = edgealgorithms[rankChosen];
                      console.log("Algorithm Chosen is "+aname);
                      function unpack(rows, key) {
                        return rows.map(function(row) { return row[key]; });
                      };
                      var col = "count"+(time%10+1);
                      var data = [{
                        mode: 'markers',
                        name: aname,
                        x: unpack(d, 'degree'),
                        y: unpack(d, col),
                        marker:{
                          color:"#eeac99"
                        }
                      }];
                      var layout = {
                        autosize: false,
                        width: 300,
                        height: testHeight,
                        xaxis: {
                          title: 'degree',
                          autorange: true,
                          //range: [0, 100]
                        },
                        yaxis: {
                          fixedrange:true, 
                          title: 'count',
                          range:[0,40]
                        },
                        margin: {
                          l: 30,
                          r: 30,
                          b: 30,
                          t: 35,
                          pad: 4
                        },
                        mode:'markers',
                        hovermode:'closest',
                        title:'Noisy Histogram',
                        showlegend: false
                      };
                      Plotly.plot('trueHist', data, layout);
                      time++;
                      var finish_time = new Date();
                     // Now we want to render a shorter algorithm name, so let's use another variable
                      short_name = ""
                      if (aname == "nodeDP_degHis_Lap") short_name = "degHis*" 
                      else if (aname == "nodeDP_degSeq_Lap") short_name = "degSeq*"
                      else if (aname == "nodeDP_nodeTrun_Smooth") short_name = "nodeTrun"
                      else if (aname == "nodeDP_edgeAdd_degHisPart_Lap") short_name = "edgeAdd_degHisPart"
                      else if (aname == "nodeDP_edgeAdd_degCum_Lap") short_name = "edgeAdd_degCum"
                      else if (aname == "nodeDP_edgeAdd_degCum_Lap_variant") short_name = "edgeAdd_degCumV"
                      else if (aname == "edgeDP_degSeq_Lap") short_name = "degSeq"
                      else if (aname == "edgeDP_degHis_Lap") short_name = "degHis"
                      else if (aname == "ladder") short_name = "Ladder"
                      else short_name = aname
                      // console.log("Time to compute is "+(finish_time - curr_time));
                      document.getElementById("noisy_explain").style.visibility = "visible";
                      document.getElementById("noisy_detail").style.visibility = "visible";
                      document.getElementById("noisy_detail").innerHTML = 
                        "Data point being displayed is algorithm: " + short_name + ". Epsilon chosen is " + eChosen;
                    });
                    if(dp_chosen == 1) var noisyHistName1 = 'uploads/'+dataChosen+"cdfalgo.csv"
                    else var noisyHistName1 = 'uploads/'+dataChosen + "cdfedgealgo.csv"
                    Plotly.d3.csv(noisyHistName1, function(err, rows){
                      var d = rows.filter(r => ((r.epsilon == eChosen) && (r.algorithm == rankChosen+1)))
                      if(dp_chosen == 1) var aname = algorithms[rankChosen]
                      else var aname = edgealgorithms[rankChosen]
                      function unpack(rows, key) {
                        return rows.map(function(row) { return row[key]; });
                      }
                      var col = "count"+(time%10+1)
                      var data = [{
                        mode: 'markers',
                        name: aname,
                        x: unpack(d, 'degree'),
                        y: unpack(d, col),
                        marker:{
                          color:"#eeac99"
                        }
                      }]
                      console.log(data);
                      var layout = {
                        autosize: true,
                        width: 300,
                        height: testHeight,
                        xaxis: {
                          type: 'log',
                          title: 'degree',
                          fixedrange:true,
                          range:[0,100]
                          //autorange: true
                        },
                        yaxis: {
                          title: 'count',
                          fixedrange: true,
                          range:[0,1]
                          //autorange: true
                        },
                        margin: {
                          l: 30,
                          r: 30,
                          b: 30,
                          t: 35,
                          pad: 4
                        },
                        mode:'markers',
                        hovermode:'closest',
                        title:'Noisy Histogram',
                        showlegend: false
                      };
                      Plotly.plot('noisyHist', data, layout);
                      time++;
                      document.getElementById("noisy_explain").style.visibility = "visible";
                      document.getElementById("noisy_detail").style.visibility = "visible";
                      document.getElementById("noisy_detail").innerHTML = "The data point being displayed is algorithm: "+aname+" ,and the epsilon chosen is "+eChosen;
                    });
                  }
                });
                
              });

            
          }
          function changevisibility(i){
            var dataChosen = '';
            var temp_data = document.getElementById("Dataset").value;
            var dp_chosen = document.getElementById("Degree Type").value;
              // dataChosen stores the dataset that user has chosen
            if (temp_data == 2) {
              dataChosen = 'CIT';
            } else if (temp_data == 3) {
              dataChosen = 'DBLP';
            } 
            else if(temp_data == 1){
              dataChosen = 'FACEBOOK';
            } else if(temp_data == 4){
              dataChosen = 'WIKI';
            } else if(temp_data == 5){
              dataChosen = 'TOYDATA';
            }
            else {
              dataChosen = 'EMAIL';
            }
              // graphSource stores the source (.png) of an image of the original dataset
            console.log(algoindex);
            var graphSource = "Plot"+dataChosen+".png";
            if(dp_chosen == 1){
              if(algoindex[i] == -1){
                algoindex[i] = i+1;
              }else{
                algoindex[i] = -1;
              }
            } else {
              if(edgealgoindex[i] == -1){
                edgealgoindex[i] = i+1;
              }
              else edgealgoindex[i] = -1;
            }
            plotfrontier(dataChosen);
          }
          function DDFn() {
            // First determine which dataset we have chosen. If none is, display empty true histogram

            // In this part we should also determine which true graphs we want to show. Set source to be NULL if no dataset is selected.
            var temp_data = document.getElementById("Dataset").value;
            var dp_chosen = document.getElementById("Degree Type").value;
            if (temp_data == 2) {
              dataChosen = 'CIT';
            } else if (temp_data == 3) {
              dataChosen = 'DBLP';
            } 
            else if(temp_data == 1){
              dataChosen = 'FACEBOOK';
            } else if(temp_data == 4){
              dataChosen = 'WIKI';
            } else if(temp_data == 5){
              dataChosen = 'TOYDATA';
            }
            else {
              dataChosen = 'EMAIL';
            }
            var cdf = 'uploads/'+dataChosen+"cdf.csv";
            if(dp_chosen == 2) var lookingname = 'uploads/'+"lookingedge.csv"
            else var lookingname = 'uploads/'+"lookingedge.csv"         
            Plotly.d3.csv(lookingname, (err, rows)=>{
              var l = rows.filter(r=>r.algo)
              algoindex = l.map(r => r.algo)
              edgealgoindex = l.map(r => r.algo);
              var k = rows.filter(r => r.algoname)
              algorithms = k.map(r=>r.algoname)
              edgealgorithms = k.map(r=>r.algoname)
            })
            //CLear the graph after a new click on the frontier; generate a random Toy dataset; Add words for the data points;
            //Challenge: upload their own algorithm
            Plotly.d3.csv(cdf, (err,rows)=>{
              function unpack(rows, key, total) {
                return rows.map(function(row) { return row[key]; });
              }
              var trace1 = {
                mode: 'markers',
                type: 'line',
                name: 'true cdf',
                x: rows.map(function(row) { return row['degree']}),
                y: unpack(rows, 'count'),
                marker: {
                  color: "#5e9aa0",
                },
              }
              var trace2 = {}
              var data = [trace1,trace2]
              var layout = {
                dragmode:"pan",
                autosize: true,
                width: 250,
                height: 300,
                xaxis: {
                  automargin: true,
                  title: {
                    text: 'degree',
                    standoff: 1,
                  },
                  type: 'log',
                  autorange: true, 
                },
                yaxis: {
                  fixedrange: true,
                  zerolin: true,
                  title: 'P(K>=k)',
                  range:[0,1]
                },
                margin: {
                  l: 30,
                  r: 30,
                  b: 30,
                  t: 35,
                  pad: 4
                },
                mode:'markers',
                hovermode:'closest',
                title:'CDF of the data',
                showlegend: false
                };
              Plotly.newPlot('noisyHist', data, layout);
            })
            
            // range, normalization of the scatter plot? Histogram shorter, name of the algorithm, number of bins smaller, button?
            //Subgraph-counting


            // The folloiwng function plots the ture DD histogram of a dataset. Note that one dataset has only one true DD. 
            var trueHistName ='uploads/'+dataChosen+'HistCSV.csv'
            Plotly.d3.csv(trueHistName, function(err, rows){
              function unpack(rows, key) {
                return rows.map(function(row) { return row[key]; });
              }

              var trace1 = {
                name: 'trueHist',
                mode: 'markers',
                type: 'bar',
                x: unpack(rows, 'degree'),
                y: unpack(rows, 'count'),
                marker: {
                  color: "#5e9aa0",
                },
              }
              var trace2 = {}
              var data = [trace1, trace2]
              var layout = {
                autosize: false,
                width: 250,
                height: 300,
                xaxis: {
                  title: 'degree',
                  fixedrange:true,
                  range:[0,100]
                  //autorange: true
                },
                yaxis: {
                  title: 'count',
                  //fixedrange:true,
                  //range:[0,40]
                  autorange:true,
                },
                margin: {
                  l: 30,
                  r: 30,
                  b: 30,
                  t: 35,
                  pad: 4
                },
                mode:'markers',
                hovermode:'closest',
                title:'Scatter Plot',
                showlegend: false
              };
              Plotly.newPlot('trueHist', data, layout)
            });
            plotfrontier(dataChosen);
            document.getElementById("show_algorithm").style.visibility = "visible";
          // Lastly, we want to update the image of the dataset by changing the source, based on variable variable "graphSource"
          //var trueGraphSource = document.getElementById("trueGraph").src;
          //document.getElementById("trueGraph").src = graphSource;
        };

        function SGCFn() {
          var temp_data = document.getElementById("Dataset").value;
          var temp_query = document.getElementById("Query").value;
          if (temp_data == 1) {
            // Tell user they need to choose a dataset.
            document.getElementById("result").innerHTML = "Dataset is not specified !";
            var dataChosen = 'EMPTY';
            var graphSource = "PlotBlank.png";
            console.log(graphSource);
          } 
          else {
            document.getElementById("result").innerHTML = "This input choice is valid.";
            
            // dataChosen stores the dataset that user has chosen
            if (temp_data == 2) {
              var dataChosen = 'CIT';
            } else if (temp_data == 3) {
              var dataChosen = 'DBLP';
            } 
            else if (temp_data == 4) {
              var dataChosen = 'FACEBOOK';
            } else {
              var dataChosen = "WIKI";
            }
            // graphSource stores the source (.png) of an image of the original dataset
            var graphSource = "Plot"+dataChosen+".png";
            // queryChosen stores the query that user has chosen
            if (temp_query == 1) {
              var queryChosen = "4kclique"
            } else if (temp_query == 2) {
              var queryChosen = "3kstar"
            } else if (temp_query == 3) {
              var queryChosen = "2ktriangle"
            } else {
              var queryChosen = "0ktriangle"
            }
          }

          // This part draws the frontier 

          var algorithms = ['Ladder', 'LAP']
          var csvName = "accuracy/"+dataChosen + queryChosen+ '.csv';
          Plotly.d3.csv(csvName, (err, rows) => {
          var tempPlot = document.getElementById('scatterFrontier')
          var data = algorithms.map(y => {
            var d = rows.filter(r => r.algorithm === y)         
            return {
              type: 'scatter',
              name: y,
              x: d.map(r => r.epsilon),
              y: d.map(r => r.relError)
            }
          })

          var layout = {
            autosize: false,
            width: 500,
            height: 300,
            xaxis: {
              type: 'log',
              autorange: true
            },
            margin: {
              l: 30,
              r: 30,
              b: 30,
              t: 35,
              pad: 4
            },
            mode:'markers',
            hovermode:'closest',
            title:'Privacy Frontier '+dataChosen
          };
          
          Plotly.newPlot('scatterFrontier', data, layout,{showSendToCloud: true});
        });
        };
        
        function frontierFn() {
          prepare();
          document.getElementById("show_algorithm").style.visibility = "visible";
          if (document.getElementById("Utility").value == 1) {
            document.getElementById("trueHist").style.visibility = "visible";
            document.getElementById("noisyHist").style.visibility = "visible";
            document.getElementById("subgraph").style.visibility = "hidden";
            document.getElementById("subgraph_png").style.height = "0px";
            DDFn();
            
          } else {
            document.getElementById("trueHist").style.visibility = "visible";
            document.getElementById("noisyHist").style.visibility = "hidden";
            // In this case we also want to set the visibility of "subgraph" to be visible
            document.getElementById("subgraph").style.visibility = "visible";
            // In addition, let's set the source for subgraph_png
            var image_name = "";
            if (document.getElementById("Utility").value == 2) {
              image_name = "triangle"
            }
            else if (document.getElementById("Utility").value == 3) {
              image_name = "3star"
            }
            else if (document.getElementById("Utility").value == 4) {
              image_name = "4clique"
            }
            else {
              image_name = "2triangle"
            }
            document.getElementById("subgraph_png").src = image_name + ".png";
            document.getElementById("subgraph_png").style.height = "60px";
            SGCFn();
          }
        }
        function buttonTextFn() {
          // The first few lines deal with button text change
          var buttonEle = document.getElementById("show_algorithm");
          // console.log(buttonEle.innerHTML);
          if (buttonEle.innerHTML =="show algorithms") {
            buttonEle.innerHTML = "hide algorithms";
          }
          else {
            buttonEle.innerHTML = "show algorithms";
          }
        }
        function animateTextFn() {
          var buttonEle = document.getElementById("gif");
          console.log(buttonEle.innerHTML);
          if (buttonEle.innerHTML.includes("Animate")) {
            buttonEle.innerHTML = "Stop";
          }
          else {
            buttonEle.innerHTML = "Animate";
          }
        }
      
      </script>
       
      <div id="DDContainer">
          <div style="float: left;" id="trueHist" class="trueHist"></div>
          <div style="float: left;" id="noisyHist" class="noisyHist"></div>
          <div style="float: left;" id="scatterFrontier"></div>
          <button 
            id = "show_algorithm" 
            onclick = "show_algorithm()"
            type="button" 
            class="btn btn-secondary"
          >
            show algorithms
          </button>
          <br>
          <form id = "select_algorithm_DD">
            <p>Please select the algorithm you want to display</p>
            <input type = "checkbox" onclick = "changevisibility(0)" id = "algorithm1">
            <span id="nodedp_algo1" style="display:inline; color:#e06377;">degHis*</span>
            <span id="edgedp_algo1" style="display:none; color:#c83349;">degHis</span><br>
            <input type = "checkbox" onclick = "changevisibility(1)" id = "algorithm2">
            <span id="nodedp_algo2" style="display:inline; color:#85E3FF;">degSeq*</span>
            <span id="edgedp_algo2" style="display:none; color:#622569;">degSeq</span><br>
            <input type = "checkbox" onclick = "changevisibility(2)" id = "algorithm3">
            <span id="edgedp_algo3" style="display:inline; color:#94b1d2;">new_algorithm</span>
            <span id="nodedp_algo3" style="display:inline; color:#b8a9c9;">nodeTrun</span><br>
            <input type = "checkbox" onclick = "changevisibility(3)" id = "algorithm4">
            <span id="nodedp_algo4" style="display:inline; color:#c83349;">edgeAdd_degHisPart</span><br>
            <input type = "checkbox" onclick = "changevisibility(4)" id = "algorithm5">
            <span id="nodedp_algo5" style="display:inline; color:#622569;">edgeAdd_degCum</span><br>
            <input type = "checkbox" onclick = "changevisibility(5)" id = "algorithm6">
            <span id="nodedp_algo6" style="display:inline; color:#3fbf5b;">edgeAdd_degCumV</span><br>
            
          </form><br>
          <br>
          <br>
          <p id="subgraph">
            The shape of the subgraph is <img id="subgraph_png" src="3star.png" alt="subgraph pic" style="width:75px;height:60px;">
          </p>
          <p id="true_explain">
            The <span style="color:#5e9aa0;font-weight:bold;">left</span> graph represents the true dataset output. 
          </p>
          <p id="noisy_explain">
            The <span style="color:#eeac99;font-weight:bold;">middle</span> graph represents the noisy dataset output.
          </p>
          <p id="noisy_detail">Data point being displayed is algorithm: . Epsilon chosen is </p>
          <?php
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
  $file = $_FILES['fileToUpload'];
  //print_r($file);

  $fileName = $_FILES['fileToUpload']['name'];
  $fileTmpName = $_FILES['fileToUpload']['tmp_name'];
  $fileSize = $_FILES['fileToUpload']['size'];
  $fileError = $_FILES['fileToUpload']['error'];
  $fileType = $_FILES['fileToUpload']['type'];
  
  $fileExt = explode('.',$fileName);
  $fileActExt = strtolower(end($fileExt));

  $allowed = array('py');
  if(in_array($fileActExt, $allowed)){
    if($fileError === 0){
      if($fileSize < 1000000){
        $fileDestination = 'uploads/new_algorithm.py';
        move_uploaded_file($fileTmpName, $fileDestination);
      } else {
        echo "Your file is too big!";
      }
    } else {
      echo "There was an error uploading the file!";
    }
  } else {
    echo "You cannot upload files of this type";
  }
}
$out = exec("uploads/create_newedge.sh 2>&1");
$empty = "";
if(empty($out)){
  echo '<script type="text/javascript">
     frontierFn()
     </script>'
;
} else {
  echo $out;
  echo '<script type="text/javascript">
  hideoption();
  </script>'
;
}
//distinguish the new algorithm - with the other type of line
//hide the first 3 algorithms
//add comments for the uploading php
//more space on the plot
?>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
        </div>
</div>
 
  <br>
  
  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>


</body>
</html>