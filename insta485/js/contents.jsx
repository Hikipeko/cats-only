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
    <div className="d-flex align-items-center">
      <a href={ownerShowUrl}>
        <img
          src={ownerImgUrl}
          className="border rounded-circle mr-3"
          alt={owner}
          style={{ height: "40px", width: "40px", objectFit: "cover" }}
        />
      </a>
      <div>
        <a href={ownerShowUrl} className="text-dark font-weight-bold">
          {owner}
        </a>
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
    <div className="card-body py-2">
      <div className="d-flex align-items-center">
        <a href={ownerShowUrl} className="d-flex align-items-center">
          <img
            src={ownerImgUrl}
            className="rounded-circle"
            alt={owner}
            style={{ height: "32px", width: "32px", objectFit: "cover", marginRight: "10px" }}
          />
        </a>
        <div>
          <a href={ownerShowUrl} className="text-dark font-weight-bold mr-2">
            {owner}
          </a>
          <span className="text-muted">• {created}</span>
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
