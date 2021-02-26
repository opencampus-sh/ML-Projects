import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from '../styles.module.css';

const TITLE = 'Machine Learning with Tensorflow Projects';
const DESCRIPTION =
  'See the awesome projects people finished during the course';
const COURSE_URL =
  'https://edu.opencampus.sh/courses/146';

import projects from '../../data/mlt/projects';

function Project({imageUrl, title, semester, students, description, project_link}) {
  const imgUrl = useBaseUrl(imageUrl);
  return (
    <div className={clsx('col col--4', styles.projects)}>
      <div className={clsx('card'), styles.proj_card}>
        <div className={"card__image", styles.card_img}>
        {imgUrl && (
          <div className="text--center">
            <img className={styles.featureImage} src={imgUrl} alt={title} />
          </div>
        )}
        </div>
        <div className={"card__body", styles.card_body}>
          <h3>{title} ({semester})</h3>
          <p className="proj_students"><i>{students}</i></p>
          <p className="proj_descr">{description}</p>
          <div className="button-group button-group--block">
            {project_link && (
              <a
                className="button button--small button--secondary button--block"
                href={project_link}
                target="_blank"
                rel="noreferrer noopener">
                Check out the Project!
              </a>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

function Home() {
  const context = useDocusaurusContext();
  const {siteConfig = {}} = context;
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <main className="container margin-vert--lg">
        <div className="text--center">
          <h1>{TITLE}</h1>
          <p>{DESCRIPTION}</p>
          <p>
            <a
              className={'button button--primary'}
              href={COURSE_URL}
              target={'_blank'}>
              Take the course and do yours!
            </a>
          </p>
        </div>
        {projects && projects.length > 0 && (
          <section className={styles.projects}>
            <div className="container">
              <div className="row">
                {projects.map((props, idx) => (
                  <Project key={idx} {...props} />
                ))}
              </div>
            </div>
          </section>
        )}
      </main>
    </Layout>
  );
}

export default Home;
