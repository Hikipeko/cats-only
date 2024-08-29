import React from "react";
import PropTypes from "prop-types";

export function PostImage(props) {
  const { imgUrl, likeEvent } = props;
  return (
    <div
      className="bg-image hover-overlay ripple rounded-0"
      data-ripple-color="light"
    >
      <img
        className="w-100"
        src={imgUrl}
        onDoubleClick={likeEvent}
        alt="post_image"
      />
      <div
        className="mask"
        style={{ backgroundColor: "rgba(251, 251, 251, 0.2)" }}
      />
    </div>
  );
}
PostImage.propTypes = {
  imgUrl: PropTypes.string.isRequired,
  likeEvent: PropTypes.func.isRequired,
};

export function Avatar(props) {
  const { ownerShowUrl, ownerImgUrl, owner } = props;
  return (
    <div className="col-md-8">
      <div className="d-flex">
        <a href={ownerShowUrl}>
          <img
            src={ownerImgUrl}
            className="border rounded-circle mr-2"
            alt="img"
            style={{ height: "40px" }}
          />
        </a>
        <div className="mt-2">
          <a href={ownerShowUrl} className="text-dark">
            <strong className="mt-5">{owner}</strong>
          </a>
        </div>
      </div>
    </div>
  );
}
Avatar.propTypes = {
  ownerShowUrl: PropTypes.string.isRequired,
  ownerImgUrl: PropTypes.string.isRequired,
  owner: PropTypes.string.isRequired,
};

export function UserInfo(props) {
  const { ownerShowUrl, ownerImgUrl, owner, postShowUrl, created } = props;
  return (
    <div className="card-body">
      <div className="container">
        <div className="row">
          <Avatar
            ownerShowUrl={ownerShowUrl}
            ownerImgUrl={ownerImgUrl}
            owner={owner}
          />
          <div className="col-md-4">
            <a href={postShowUrl}>
              <p className="mt-2 float-right" style={{ color: "grey" }}>
                {created}
              </p>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
UserInfo.propTypes = {
  ownerShowUrl: PropTypes.string.isRequired,
  ownerImgUrl: PropTypes.string.isRequired,
  owner: PropTypes.string.isRequired,
  postShowUrl: PropTypes.string.isRequired,
  created: PropTypes.string.isRequired,
};
