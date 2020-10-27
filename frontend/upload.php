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
            <a class="nav-link" href="performance.html">Performance Frontier</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownPortfolio" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Empirical Findings
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownPortfolio">
              <a class="dropdown-item" href="finding.html">Finding Overview</a>
              <a class="dropdown-item" href="#">Competitive Algorithm</a>
              <a class="dropdown-item" href="#">Effect of Data Shape</a>
              <a class="dropdown-item" href="#">Comparison Against Baseline</a>
            </div>
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
        <option value = "1" selected = "selected">Node DP</option>
        
        </select>

        <select id = "Utility"> 
        <option value = "1" selected = "selected">Degree Distribution</option>
        <option value = "2">Subgraph Counting_4kclique</option>
        <option value = "3">Subgraph Counting_3kstar</option>
        <option value = "4">Subgraph Counting_2ktriangle</option>
        <option value = "5">Subgraph Counting_0ktriangle</option>
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
        document.getElementById("algorithm7").style.visibility = "hidden";
        document.getElementById("algorithm2").checked = true;
        document.getElementById("algorithm7").checked = true;
        document.getElementById("algorithm3").checked = true;
        document.getElementById("algorithm4").checked = true;
        document.getElementById("algorithm5").checked = true;
        document.getElementById("algorithm6").checked = true;
      }
 
  function prepare(){
    hideoption();
    document.getElementById("gif").style.visibility = "hidden";
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
            var dp_chosen = document.getElementById("Degree Type").value;
            if(document.getElementById("select_algorithm_DD").style.visibility != "visible"){
              document.getElementById("select_algorithm_DD").style.visibility = "visible";
              document.getElementById("algorithm3").style.visibility = "visible";
              document.getElementById("algorithm4").style.visibility = "visible";
              document.getElementById("algorithm5").style.visibility = "visible";
              document.getElementById("algorithm6").style.visibility = "visible";
              document.getElementById("algorithm1").style.visibility = "visible";
              document.getElementById("algorithm2").style.visibility = "visible";
              document.getElementById("algorithm7").style.visibility = "visible";
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
                document.getElementById("algorithm7").style.visibility = "visible";
                document.getElementById("nodedp_algo7").style.display = "inline";
              } 
              else {
                document.getElementById("nodedp_algo1").style.display = "none";
                document.getElementById("edgedp_algo1").style.display = "inline";
                document.getElementById("nodedp_algo2").style.display = "none";
                document.getElementById("edgedp_algo2").style.display = "inline";
                document.getElementById("algorithm3").style.visibility = "hidden";
                document.getElementById("nodedp_algo3").style.display = "none";
                document.getElementById("algorithm4").style.visibility = "hidden";
                document.getElementById("nodedp_algo4").style.display = "none";
                document.getElementById("algorithm5").style.visibility = "hidden";
                document.getElementById("nodedp_algo5").style.display = "none";
                document.getElementById("algorithm6").style.visibility = "hidden";
                document.getElementById("nodedp_algo6").style.display = "none";
                document.getElementById("algorithm7").style.visibility = "hidden";
                document.getElementById("nodedp_algo7").style.display = "none";
              }
            } else {
              document.getElementById("select_algorithm_DD").style.visibility = "hidden";
              document.getElementById("algorithm3").style.visibility = "hidden";
              document.getElementById("algorithm4").style.visibility = "hidden";
              document.getElementById("algorithm5").style.visibility = "hidden";
              document.getElementById("algorithm6").style.visibility = "hidden";
              document.getElementById("algorithm1").style.visibility = "hidden";
              document.getElementById("algorithm2").style.visibility = "hidden";
              document.getElementById("algorithm7").style.visibility = "hidden";
            }
          }
          function plotfrontier(dataChosen){
            var dp_chosen = document.getElementById("Degree Type").value;
            if(dp_chosen == 2) var csvName = 'uploads/'+dataChosen + 'edge.csv';
            else var csvName = 'uploads/'+dataChosen + '.csv';
            
            Plotly.d3.csv(csvName, (err, rows) => {
              var tempPlot = document.getElementById('scatterFrontier')
              function getcolor(y){
                if(y==1)return "blue";
                else if(y==2) return "orange";
                else if(y==3) return "green";
                else if(y==4) return "red";
                else if(y==5) return "purple";
                else if(y==6) return "brown";
                else if(y==7) return "pink";
              }
              console.log(algoindex)
              if(dp_chosen == 1){
                function getwidth(y){
                  if(y==7)return 3;
                  else return 1;
                }
                var data = algoindex.map(y => {
                  var d = rows.filter(r => r.algorithm == y)    
                  return {
                    name: algorithms[y-1],
                    x: d.map(r => r.epsilon),
                    y: d.map(r => r.L1error),
                    color: getcolor(y),
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
                    color: getcolor(y),
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
              var layout = {
                autosize: false,
                width: 300,
                height: 300,
                xaxis: {
                  type: 'log',
                  title: 'epsilon',
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
                  title: 'L1error',
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
                  
                },
                colorway:["blue","orange","green","red","purple","brown"],
                margin: {
                  l: 30,
                  r: 30,
                  b: 30,
                  t: 35,
                  pad: 4
                },
                mode:'markers',
                hovermode:'closest',
                title:'Privacy Frontier '+dataChosen,
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
                  document.getElementById("gif").style.visibility = "visible"
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
                        y: unpack(d, col)
                      }];
                      var layout = {
                        autosize: false,
                        width: 300,
                        height: testHeight,
                        xaxis: {
                          title: 'degree',
                          autorange: false,
                          range: [0, 300]
                        },
                        yaxis: {
                          fixedrange:true, 
                          title: 'count',
                          autorange: true,
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
                      console.log("Time to compute is "+(finish_time - curr_time));
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
                        y: unpack(d, col)
                      }]
                      console.log(data);
                      var layout = {
                        autosize: true,
                        width: 300,
                        height: testHeight,
                        xaxis: {
                          type: 'log',
                          title: 'degree',
                          //autorange: true
                        },
                        yaxis: {
                          title: 'count',
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
            else var lookingname = 'uploads/'+"looking.csv"         
            Plotly.d3.csv(lookingname, (err, rows)=>{
              var l = rows.filter(r=>r.algo)
              algoindex = l.map(r => r.algo)
              edgealgoindex = l.map(r => r.algo);
              var k = rows.filter(r => r.algoname)
              algorithms = k.map(r=>r.algoname)
              edgealgorithms = k.map(r=>r.algoname)
              algoindex[0] = -1;
              algoindex[1] = -1;
              algoindex[2] = -1;
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
                y: unpack(rows, 'count')
              }
              var trace2 = {}
              var data = [trace1,trace2]
              var layout = {
                autosize: true,
                width: 250,
                height: 300,
                xaxis: {
                  title: 'degree',
                  type: 'log',
                  autorange: true
                },
                yaxis: {
                  fixedrange: true,
                  zerolin: true,
                  type: 'log',
                  title: 'P(K>=k)',
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
                y: unpack(rows, 'count')
              }
              var trace2 = {}
              var data = [trace1, trace2]
              var layout = {
                autosize: false,
                width: 250,
                height: 300,
                xaxis: {
                  title: 'degree',
                  range: getxrange(),
                  //autorange: true
                },
                yaxis: {
                  title: 'count',
                  range: getyrange()
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
        var animation = 1;
        function started(){  
          if(animation == 1){
            console.log("start");
            animation = 2;
            time = 6;
            gif(1);
          } else {
            animation = 1;
            console.log("stop")
            time = 11;
          }
        }
        function gif(type_chosen){
          if(time >10) return;
          var dataChosen = '';
          var dp_chosen = document.getElementById("Degree Type").value;
          var temp_data = document.getElementById("Dataset").value;
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
          if(dp_chosen == 1 && type_chosen == 1) var noisyHistName = dataChosen+"algo.csv"
          else if(dp_chosen == 2 && type_chosen == 1)var noisyHistName = dataChosen + "edgealgo.csv"
          else if(dp_chosen == 1 && type_chosen == 2)var noisyHistName = dataChosen + "cdfalgo.csv"
          else var noisyHistName = dataChosen + "cdfedgealgo.csv"
          Plotly.d3.csv(noisyHistName, function(err, rows){
            var d = rows.filter(r => ((r.epsilon == eChosen) && (r.algorithm == rankChosen+1)))
            if(dp_chosen == 1) var aname = algorithms[rankChosen]
            else var aname = edgealgorithms[rankChosen]
            function unpack(rows, key) {
              return rows.map(function(row) { return row[key]; });
            }
            var col = "count"+time
            console.log(col)
            if(time >10) return;
            var data = [{
              mode: 'markers',
              name: "test",
              x: unpack(d, 'degree'),
              y: unpack(d, col)
            }]
            var layout = {
              autosize: true,
              width: 300,
              height: 300,
              xaxis: {
                type: 'log',
                title: 'degree',
                          //autorange: true
              },
              yaxis: {
                title: 'count',
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
            if(type_chosen == 1){
              Plotly.deleteTraces('trueHist', 1);
              Plotly.plot('trueHist', data, layout);
            } else {
              Plotly.deleteTraces('noisyHist', 1);
              Plotly.plot('noisyHist', data, layout);
            }            
            if(type_chosen == 2) time++;
            if(time == 11) time = 1;
            if(type_chosen == 1) gif(2);
            else gif(1)
          })
          
          
        }
        function frontierFn() {
          prepare();
          document.getElementById("show_algorithm").style.visibility = "visible";
          document.getElementById("Utility").style.visibility = "visible";
          document.getElementById("Degree Type").style.visibility = "visible";
          document.getElementById("Dataset").style.visibility = "visible";
          if (document.getElementById("Utility").value == 1) {
            document.getElementById("trueHist").style.visibility = "visible";
            document.getElementById("noisyHist").style.visibility = "visible";
            DDFn();
            
          } else {
            document.getElementById("trueHist").style.visibility = "hidden";
            document.getElementById("noisyHist").style.visibility = "hidden";
            SGCFn();
          }
        }
      
      </script>
       
      <div id="DDContainer">
          <div style="float: left;" id="trueHist" class="trueHist"></div>
          <div style="float: left;" id="noisyHist" class="noisyHist"></div>
          <div style="float: left;" id="scatterFrontier"></div>
          <button id = "show_algorithm" onclick = "show_algorithm()">show algorithms</button><br>
          <form id = "select_algorithm_DD">
            <p>Please select the algorithm you want to display</p>
            <input type = "checkbox" onclick = "changevisibility(0)" id = "algorithm1">
            <span id="nodedp_algo1" style="display:inline; color:blue;">degHis_Lap.</span>
            <span id="edgedp_algo1" style="display:none; color:blue;">degHis_Lap</span><br>
            <input type = "checkbox" onclick = "changevisibility(1)" id = "algorithm2">
            <span id="nodedp_algo2" style="display:inline; color:orange;">degSeq_Lap</span>
            <span id="edgedp_algo2" style="display:none; color:orange;">degSeq_Lap</span><br>
            <input type = "checkbox" onclick = "changevisibility(2)" id = "algorithm3">
            <span id="nodedp_algo3" style="display:inline; color:green;">nodeTrun_Smooth</span><br>
            <input type = "checkbox" onclick = "changevisibility(3)" id = "algorithm4">
            <span id="nodedp_algo4" style="display:inline; color:red;">edgeAdd_degHisPart_Lap</span><br>
            <input type = "checkbox" onclick = "changevisibility(4)" id = "algorithm5">
            <span id="nodedp_algo5" style="display:inline; color:purple;">edgeAdd_degCum_Lap</span><br>
            <input type = "checkbox" onclick = "changevisibility(5)" id = "algorithm6">
            <span id="nodedp_algo6" style="display:inline; color:brown;">edgeAdd_degCum_Lap_variant</span><br>
            <input type = "checkbox" onclick = "changevisibility(6)" id = "algorithm7">
            <span id="nodedp_algo7" style="display:inline; color:blue;">new_algorithm</span><br>
          </form><br>
          <br>
          <br>
          <button id="gif" onclick="started()">Animate</button>
          <p id="true_explain">The <span style="color:blue;font-weight:bold;">blue</span> graph represent the true dataset. </p>
          <p id="noisy_explain">The <span style="color:orange;font-weight:bold;">orange</span> graph represent the noisy dataset</p>
          <p id="noisy_detail">The data point being displayed is algorithm: ,and the epsilon chosen is </p>
          <?php
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
  $file = $_FILES[‘filesToUpload’];
  print_r($file);

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
$out = exec("uploads/create_new.sh 2>&1");
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