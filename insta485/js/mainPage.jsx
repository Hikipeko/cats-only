import React from "react";
import InfiniteScroll from "react-infinite-scroll-component";
import Post from "./post";

class MainPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      results: [],
      next: "/api/v1/posts/",
    };
    this.getPosts = this.getPosts.bind(this);
  }

  componentDidMount() {
    this.getPosts();
  }

  getPosts() {
    const { results, next } = this.state;
    if (next === "") {
      return;
    }
    fetch(next, { credentials: "same-origin" })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          results: results.concat(data.results),
          next: data.next,
        });
      })
      .catch((error) => console.log(error));
  }

  render() {
    const { results, next } = this.state;
    const listItems = results.map((post) => (
      <Post url={post.url} key={post.postid} />
    ));
    return (
      <div className="container my-1">
        <div className="row">
          <div className="col-md-3" />
          <div className="col-md-6">
            <InfiniteScroll
              dataLength={listItems.length}
              next={this.getPosts}
              hasMore={next !== ""}
              loader={<h4>Loading...</h4>}
            >
              {listItems}
            </InfiniteScroll>
          </div>
          <div className="col-md-3" />
        </div>
      </div>
    );
  }
}

MainPage.propTypes = {};
export default MainPage;
