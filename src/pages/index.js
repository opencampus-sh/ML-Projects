import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const features = [
  {
    title: 'Deep Learning',
    imageUrl: 'https://edu.opencampus.sh/courses/146/medium.jpg',
    directionUrl: "/dl",
    description: (
      <>
        The Deep Learning Course focused on learning the basics of neural networks starting from scratch.
      </>
    ),
  },
  {
    title: 'Machine Learning with Tensorflow',
    imageUrl: 'https://edu.opencampus.sh/courses/147/medium.jpg',
    directionUrl: "/mlt",
    description: (
      <>
        The Tensorflow Course focused on using the popular open-source framework for creating machine learning projects.
      </>
    ),
  },
  {
    title: 'Natural Language Processing',
    imageUrl: 'https://edu.opencampus.sh/courses/160/medium.jpg',
    directionUrl: "/nlp",
    description: (
      <>
        The Natural Language Processing Course focused on using neural network to analyze and process text.
      </>
    ),

  },
];

function Feature({imageUrl, title, description, directionUrl}) {
  const imgUrl = useBaseUrl(imageUrl);
  return (

      <div className={clsx('col col--4', styles.feature)}>
        <a href={directionUrl}>
        {imgUrl && (
          <div className="text--center">
            <img className={styles.featureImage} src={imgUrl} alt={title} />
          </div>
        )}
        <h3>{title}</h3>
        <p>{description}</p>
        </a>
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
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <h1 className="hero__title">{siteConfig.title}</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className={clsx(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
              to="https://edu.opencampus.sh/courses/158">
              Done with the projects. Take me to the Degree to enroll!
            </Link>
          </div>
        </div>
      </header>
      <main>
        {features && features.length > 0 && (
          <section className={styles.features}>
            <div className="container">
              <div className="row">
                {features.map((props, idx) => (
                  <Feature key={idx} {...props} />
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
